import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { BackendApiService } from '../core/service/backend-api.service';
import { DropdownComponent } from '../components/dropdown/dropdown';
import { FilterStringFieldModel } from '../model/filter-string-field.model';

@Injectable({
  providedIn: 'root',
})
export class ContainFieldService {
  

  private api = inject(BackendApiService);
  private endpoint = 'filter/filter_field_unique_values';
  
  
  createContainField(field: string): Observable<string[]> {

    const params = new HttpParams().set('field', field);

    return this.api.get<string[]>(this.endpoint,  params);
  }

}

