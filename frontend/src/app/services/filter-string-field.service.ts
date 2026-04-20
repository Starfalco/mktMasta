import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { FilterStringFieldModel } from '../model/filter-string-field.model';

@Injectable({
  providedIn: 'root',
})
export class FilterStringFieldService {
  private api = inject(BackendApiService);

  private endpoint = 'filter/filter_string_field';

  createFilterStringField(filterStringField: Partial<FilterStringFieldModel>): Observable<FilterStringFieldModel> {
    return this.api.post<FilterStringFieldModel>(this.endpoint, filterStringField);
  }

}
