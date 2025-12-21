import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { scopes } from '../model/scopesMod.type';

@Injectable({
  providedIn: 'root'
})
export class RetrieveScope {
  http = inject(HttpClient);

  getScopesFromApi() {
    const url = `http://localhost:8000/retrieve/scope`

    return this.http.get<Array<scopes>>(url);
    
  }

  getDataBySymbol(symbol: string) {
      const url = `http://localhost:8000/retrieve/data`;

      return this.http.get<any>(url, {
        params: { symbol }
      });
    }
  };