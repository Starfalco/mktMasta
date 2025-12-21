import { Injectable } from '@angular/core';
import { prices } from '../model/prices';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private apiUrl = 'http://localhost:8000/retrieve/retrieve_price'; 

  constructor(private http: HttpClient) {}

  getItem(itemId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/${itemId}`);
  }
}





