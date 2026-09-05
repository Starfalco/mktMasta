"""
Rate limiter and retry utility for yfinance API calls.

Provides:
- Global request serialization (only 1 request at a time across all threads)
- Configurable delay between requests
- Exponential backoff with jitter for retries
- Thread-safe session management
"""

import time
import random
import threading
from functools import wraps

from curl_cffi import requests as curl_requests


class RateLimiter:
    """
    Configurable rate limiter for API requests.

    Uses a global lock to ensure only ONE request is made at a time across
    all threads. This is the most reliable way to avoid rate limits.

    Usage:
        limiter = RateLimiter(request_delay=0.5, max_retries=3)
        session = limiter.get_session()

        # Or use the decorator for individual functions
        @limiter.retry_on_rate_limit()
        def fetch_data(ticker):
            ...
    """

    def __init__(
        self,
        request_delay: float = 0.5,
        max_retries: int = 3,
        base_delay: float = 2.0,
        max_delay: float = 60.0,
        jitter: bool = True,
    ):
        """
        Args:
            request_delay: Fixed delay between requests (seconds).
                          Lower = faster but higher risk of rate limits.
            max_retries: Max number of retries on rate limit errors
            base_delay: Initial delay between retries (seconds)
            max_delay: Maximum delay between retries (seconds)
            jitter: Add random jitter to delays to avoid thundering herd
        """
        self.request_delay = request_delay
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter

        # Global lock to serialize ALL requests across all threads
        self._lock = threading.Lock()

        # Thread-local storage for sessions
        self._local = threading.local()

    def get_session(self):
        """Get a session with Chrome impersonation (thread-safe)."""
        if not hasattr(self._local, 'session'):
            self._local.session = curl_requests.Session(impersonate="chrome")
            self._local.session.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                               "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        return self._local.session

    def retry_on_rate_limit(self, func=None, max_retries=None, base_delay=None):
        """
        Decorator that adds global serialization + exponential backoff retry.

        The global lock ensures only ONE request runs at a time across all threads.

        Usage:
            @rate_limiter.retry_on_rate_limit()
            def fetch_ticker(ticker):
                return yf.Ticker(ticker).info
        """
        def decorator(fn):
            retries = max_retries or self.max_retries
            delay = base_delay or self.base_delay

            @wraps(fn)
            def wrapper(*args, **kwargs):
                for attempt in range(retries + 1):
                    try:
                        # Acquire global lock - only one request at a time
                        with self._lock:
                            # Enforce delay between requests
                            time.sleep(self.request_delay)
                            return fn(*args, **kwargs)
                    except Exception as e:
                        error_msg = str(e).lower()
                        # Check if this is a rate limit error
                        is_rate_limit = any(keyword in error_msg for keyword in [
                            '429', 'rate limit', 'too many requests',
                            'ratelimited', 'rate limited', 'temporarily unavailable'
                        ])

                        if not is_rate_limit or attempt == retries:
                            raise

                        # Extract ticker from args (args[0] is self, args[1] is ticker)
                        ticker = args[1] if len(args) > 1 else kwargs.get('ticker', 'unknown')

                        # Calculate delay with exponential backoff + jitter
                        exponential_delay = delay * (2 ** attempt)
                        final_delay = min(exponential_delay, self.max_delay)
                        if self.jitter:
                            final_delay = final_delay * random.uniform(0.5, 1.5)

                        print(f"Rate limit hit for {ticker}, "
                              f"retry {attempt + 1}/{retries} in {final_delay:.1f}s")
                        time.sleep(final_delay)

                return None

            return wrapper
        return decorator if func is None else func(func)


# Default rate limiter instance (0.5s delay between requests, 3 retries)
default_rate_limiter = RateLimiter(
    request_delay=0.5,
    max_retries=3,
    base_delay=2.0,
    max_delay=60.0,
)
