import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { InitCacheModel } from '../model/init-cache.model';
import { ConfigService } from './config-file-service';

@Injectable({
  providedIn: 'root'
})
export class InitCacheService {
  private api = inject(BackendApiService);

  private endpoint = 'cache/init_cache';

  initCache() {
  const endpoint = this.config.backendApi.endpointInitCache;
  return this.post(endpoint, {});
}
  }
