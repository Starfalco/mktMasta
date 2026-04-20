import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { RetrieveCacheModel } from '../model/retrieve-cache.model';

@Injectable({
  providedIn: 'root'
})
export class RetrieveCachesService {
  private api = inject(BackendApiService);
  private endpoint = 'cache/retrieve_cache';

  // getRetrieveCache(): Observable<RetrieveCacheModel[]> {
  //   return this.api.get<RetrieveCacheModel[]>(this.endpoint);
  // }
  getRetrieveCache(): Observable<RetrieveCacheModel[]> {
  const obs$ = this.api.get<RetrieveCacheModel[]>(this.endpoint);

  obs$.subscribe({
    next: data => console.log('API response:', data),
    error: err => console.error('API error:', err)
  });

  return obs$;
}
}