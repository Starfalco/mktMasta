import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ConfigService } from '../../services/config-file-service';


@Injectable({
  providedIn: 'root'
})
export class BackendApiService {
  private config = inject(ConfigService);
  private http = inject(HttpClient);

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'Content-Type': 'application/json'
    });
  }

  get<T>(endpoint: string, params?: HttpParams): Observable<T> {
    return this.http.get<T>(this.config.getApiUrl(endpoint), {
      headers: this.getHeaders(),
      params,
    });
  }


  // get<T>(endpoint: string): Observable<T> {
  //   return this.http.get<T>(this.config.getApiUrl(endpoint));
  // }
  post<T>(endpoint: string, body: any, params?: HttpParams): Observable<T> {
    return this.http.post<T>(this.config.getApiUrl(endpoint), body, {
      headers: this.getHeaders(),
      params,
      withCredentials: true
    });
  }

  put<T>(endpoint: string, body: any): Observable<T> {
    return this.http.put<T>(this.config.getApiUrl(endpoint), body, {
      headers: this.getHeaders(),
    });
  }

  delete<T>(endpoint: string): Observable<T> {
    return this.http.delete<T>(this.config.getApiUrl(endpoint), {
      headers: this.getHeaders(),
    });
  }

}
