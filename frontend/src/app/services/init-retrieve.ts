import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class RetrieveCacheService {
  http=inject(HttpClient);

  RetrieveCache(){
    const  url  ='http://localhost:8000/cache/retrieve_cache'

    return this.http.get(url);
  }
}