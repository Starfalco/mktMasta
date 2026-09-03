import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';

import { ConfigService } from './config-file-service';

describe('ConfigService', () => {
  let service: ConfigService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [],
      providers: [
        provideHttpClient(),
        provideRouter([])
      ]
    });
    service = TestBed.inject(ConfigService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return empty baseUrl before config loads', () => {
    expect(service.getBaseUrl()).toBe('');
  });

  it('should return fallback apiUrl for relative paths', () => {
    expect(service.getApiUrl('cache/init_cache')).toBe('/cache/init_cache');
  });
});
