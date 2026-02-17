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

   getPriceBySymbol(ticker: string) {
    const url = `http://localhost:8000/retrieve/retrieve_price/${ticker}`;
    return this.http.get<prices[]>(url);
      }
      
   getEarningEstBySymbol(ticker: string) {
    const url = `http://localhost:8000/retrieve/earnings_estimate/${ticker}`;
    return this.http.get<Earning[]>(url);
      }      
   getEarningHistBySymbol(ticker: string) {
    const url = `http://localhost:8000/retrieve/earnings_history/${ticker}`;
    return this.http.get<price[]>(url);
      }            
      ;
    }
  ;