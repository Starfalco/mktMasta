import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { RetrieveCacheModel } from '../model/retrieve-cache.model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RetrieveCachesService {
//   private api = inject(BackendApiService);
//   private endpoint = 'cache/retrieve_cache';

//   getRetrieveCache(): Observable<RetrieveCacheModel[]> {
//     return this.api.get<RetrieveCacheModel[]>(this.endpoint);
//   }

  http = inject(HttpClient);

  getRetrieveCache() {
    const url = `http://localhost:8000/cache/retrieve_cache`

    return this.http.get<Array<RetrieveCacheModel>>(url);
    
  }




}