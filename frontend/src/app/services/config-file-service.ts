import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ConfigService {
  private config: any;

  constructor(private http: HttpClient) {}

  loadConfig(): Promise<void> {
    return this.http.get('/configsrc.json')
      .toPromise()
      .then((data) => {
        this.config = data;
      });
  }

  get backendApi() {
    return this.config?.backendApi;
  }

  
}