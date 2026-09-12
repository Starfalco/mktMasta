import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface BackendApiConfig {
  baseUrl: string;
  httpHeader: string;
  endpointInitCache: string;
  endpointRetrieveCache: string;
  endpointFilterFieldUniqueValues: string;
}

export interface AppConfig {
  backendApi: BackendApiConfig;
}

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  private http = inject(HttpClient);
  private config: AppConfig | null = null;
  private configLoaded = false;

  /**
   * Fetches the app config from the backend at runtime.
   *
   * The backend serves this at /config.json. When frontend_base_url is empty
   * in the backend settings, baseUrl is '' so the frontend uses relative paths
   * (ideal for reverse-proxy deployments behind Nginx/Apache).
   *
   * Call this early in the app lifecycle before making API calls.
   */
  loadConfig(): Promise<AppConfig> {
    if (this.configLoaded && this.config) {
      return Promise.resolve(this.config);
    }

    return new Promise<AppConfig>((resolve, reject) => {
      this.http.get<AppConfig>('/config.json')
        .subscribe({
          next: (config) => {
            this.config = config;
            this.configLoaded = true;
            resolve(config);
          },
          error: (error) => {
            console.error('Failed to load config from backend, using fallback.', error);
            // Fallback: use relative paths (works when frontend and backend share a domain)
            this.config = {
              backendApi: {
                baseUrl: '',
                httpHeader: 'Content-Type: application/json',
                endpointInitCache: 'cache/init_cache',
                endpointRetrieveCache: 'cache/retrieve_cache',
                endpointFilterFieldUniqueValues: 'filter/filter_field_unique_values'
              }
            };
            this.configLoaded = true;
            reject(error);
          }
        });
    });
  }

  getBaseUrl(): string {
    return this.config?.backendApi.baseUrl ?? '';
  }

  getHttpHeader(): string {
    return this.config?.backendApi.httpHeader ?? 'Content-Type: application/json';
  }

  /**
   * Builds a full API URL by combining baseUrl with an endpoint path.
   * Handles both absolute URLs and relative paths.
   */
  getApiUrl(endpoint: string): string {
    const base = this.getBaseUrl();
    if (!base) {
      // Relative path — works with reverse proxy
      return `/${endpoint}`;
    }
    // Ensure no double slashes
    return `${base.replace(/\/$/, '')}/${endpoint.replace(/^\//, '')}`;
  }
}
