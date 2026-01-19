import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class InitCacheService {
  http=inject(HttpClient);

  InitCache(){
    const  url  ='http://localhost:8000/cache/init_cache/'

    return this.http.get(url);
  }
}