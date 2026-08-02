import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpParams } from '@angular/common/http';
import { BackendApiService } from '../core/service/backend-api.service';


@Injectable({
  providedIn: 'root',
})
export class SortByFieldsService {


  private api = inject(BackendApiService);

  private endpoint = 'sort/sort_by_fields';



  sortByField(
    field: string,
    ascending: boolean
  ): Observable<void> {


    const params = new HttpParams()
      .set(
        'ascending_sort',
        ascending.toString()
      );


    const body = [
      field
    ];



    console.log('SORT BODY:', body);

    console.log('SORT PARAMS:', params.toString());



    return this.api.post<void>(
      this.endpoint,
      body,
      params
    );

  }

}