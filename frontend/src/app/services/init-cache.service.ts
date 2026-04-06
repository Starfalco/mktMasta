import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { InitCacheModel } from '../model/init-cache.model';

@Injectable({
  providedIn: 'root'
})
export class InitCacheService {
  private api = inject(BackendApiService);

  private endpoint = 'cache/init_cache';

  getInitCaches(): Observable<InitCacheModel[]> {
    return this.api.get<InitCacheModel[]>(this.endpoint);
  }
}