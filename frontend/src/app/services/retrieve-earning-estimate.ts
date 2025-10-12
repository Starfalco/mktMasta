import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Earning } from '../model/earning.type';

@Injectable({
  providedIn: 'root'
})
export class RetrieveEarningEstimate {
  http = inject(HttpClient);

  getEarningFromApi() {
    const url = `http://localhost:8000/retrieve/earnings_estimate`

    return this.http.get<Array<Earning>>(url);
  }
}
