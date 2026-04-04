import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { scopes } from '../model/scopesMod.type';


@Injectable({
  providedIn: 'root'
})
export class EarningDateServe {
  http=inject(HttpClient);

  retrieveDates(){
    const  url  =`http://localhost:8000/extract/extracts_earnings_dates`

    return this.http.get<Array<scopes>>(url);
  }
}
