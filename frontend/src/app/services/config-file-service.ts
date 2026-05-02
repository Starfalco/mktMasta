import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import config from '../../assets/configsrc.json';


@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  private config = config;

  getBaseUrl(): string {
    return this.config.backendApi.baseUrl;
  }

  // Optionally, add more methods for other values
  getHttpHeader(): string {
    return this.config.backendApi.httpHeader;
  }
}

// export class ConfigService {
//   private config: any;

//   constructor(private http: HttpClient) {}

  // loadConfig(): Promise<void> {
  //   return this.http.get('../../../public/configsrc.json')
  //     .toPromise()
  //     .then((data) => {
  //       this.config = data;
  //     });
  // }
      // loadConfig() {
      //   const url = `assets/configsrc.json`

      //   return this.http.get(url);
       

      // }
         
  // backendApi(): Promise<void>  {
  //   return this.loadConfig();
  // }
// getRetrieveCache() {
  //   const url = `http://localhost:8000/cache/retrieve_cache`

  //   return this.http.get<Array<RetrieveCacheModel>>(url);
    
  
// }