import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs'; // ✅ Import this
import { price } from '../../model/price.type';

@Injectable({
  providedIn: 'root'
})
export class APIServiceService {
  constructor(private http: HttpClient) { }

  getData(): Promise<any> {
    return firstValueFrom(this.http.get('http://localhost:8000/retrieve/earnings_history'));
  }
}