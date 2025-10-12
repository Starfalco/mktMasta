import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs'; // ✅ Import this
import { Earning } from '../../model/earning.type';

@Injectable({
  providedIn: 'root'
})
export class APIServiceService {
  constructor(private http: HttpClient) { }

  getData(): Promise<any> {
    return firstValueFrom(this.http.get('http://localhost:8000/retrieve/earnings_estimate'));
  }
}