import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { FilterNumericFieldModel } from '../model/filter-numeric-field.model';

@Injectable({
  providedIn: 'root',
})
export class FilterNumericFieldService {
  private api = inject(BackendApiService);

  private endpoint = 'filter/filter_numeric_field';

  createFilterNumericField(filterNumericField: Partial<FilterNumericFieldModel>): Observable<modelFilterNumericField> {
    return this.api.post<FilterNumericFieldModel>(this.endpoint, filterNumericField);
  }

}
