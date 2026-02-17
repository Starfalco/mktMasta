import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { backendApi } from '../core/service/backendapi';
import { Observable } from 'rxjs';
import { modelRetrieveCache } from '../model/modelRetrieveCache.type';


@Injectable({
  providedIn: 'root'
})
export class modelRetrieveCachesService {
  private api = inject(backendApi);
  private endpoint = 'modelRetrieveCaches';

  getmodelRetrieveCaches(): Observable<modelRetrieveCache[]> {
    return this.api.get<modelRetrieveCache[]>(this.endpoint);
  }

  // getmodelRetrieveCache(id: number): Observable<modelRetrieveCache> {
  //   return this.api.get<modelRetrieveCache>(`${this.endpoint}/${id}`);
  // }

  // createmodelRetrieveCache(modelRetrieveCache: Partial<modelRetrieveCache>): Observable<modelRetrieveCache> {
  //   return this.api.post<modelRetrieveCache>(this.endpoint, modelRetrieveCache);
  // }

  // updatemodelRetrieveCache(id: number, modelRetrieveCache: Partial<modelRetrieveCache>): Observable<modelRetrieveCache> {
  //   return this.api.put<modelRetrieveCache>(`${this.endpoint}/${id}`, modelRetrieveCache);
  // }

  // deletemodelRetrieveCache(id: number): Observable<void> {
  //   return this.api.delete<void>(`${this.endpoint}/${id}`);
  // }
}