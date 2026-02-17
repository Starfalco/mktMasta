import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { backendApi } from '../core/service/backendapi';
import { Observable } from 'rxjs';
import { modelInitCache } from '../model/modelinitcache.model';



@Injectable({
  providedIn: 'root'
})
export class modelInitCachesService {
  private api = inject(backendApi);
  
  private endpoint = 'cache/init_cache';

  getmodelInitCaches(): Observable<modelInitCache[]> {
    return this.api.get<modelInitCache[]>(this.endpoint);
  }

  // getmodelInitCache(id: number): Observable<modelInitCache> {
  //   return this.api.get<modelInitCache>(`${this.endpoint}/${id}`);
  // }

  // createmodelInitCache(modelInitCache: Partial<modelInitCache>): Observable<modelInitCache> {
  //   return this.api.post<modelInitCache>(this.endpoint, modelInitCache);
  // }

  // updatemodelInitCache(id: number, modelInitCache: Partial<modelInitCache>): Observable<modelInitCache> {
  //   return this.api.put<modelInitCache>(`${this.endpoint}/${id}`, modelInitCache);
  // }

  // deletemodelInitCache(id: number): Observable<void> {
  //   return this.api.delete<void>(`${this.endpoint}/${id}`);
  // }
}