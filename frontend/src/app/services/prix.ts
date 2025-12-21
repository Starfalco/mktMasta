import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { scopes } from '../model/scopesMod.type';
import { prices } from '../model/prices';
import { Earning } from '../model/earning.type';
import { price } from '../model/price.type';

@Injectable({
  providedIn: 'root'
})
export class RetrievePrix {
  http = inject(HttpClient);

  getScopesFromApi() {
    const url = `http://localhost:8000/retrieve/scope`

    return this.http.get<Array<scopes>>(url);
    
  }

   getPriceBySymbol(symbol: string) {
    const url = `http://localhost:8000/retrieve/retrieve_price/${symbol}`;
    return this.http.get<prices[]>(url);
      }
      
   getEarningEstBySymbol(symbol: string) {
    const url = `http://localhost:8000/retrieve/earnings_estimate/${symbol}`;
    return this.http.get<Earning[]>(url);
      }      
   getEarningHistBySymbol(symbol: string) {
    const url = `http://localhost:8000/retrieve/earnings_history/${symbol}`;
    return this.http.get<price[]>(url);
      }            
      ;
    }
  ;