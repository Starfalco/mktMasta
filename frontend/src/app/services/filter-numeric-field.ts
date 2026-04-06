import { inject, Injectable } from '@angular/core';
import { backendApi } from '../core/service/backendapi';
import { Observable } from 'rxjs';
import { modelFilterNumericField } from '../model/filter-numeric-field.model.ts';

@Injectable({
  providedIn: 'root',
})
export class FilterNumericField {
  private api = inject(backendApi);

  private endpoint = 'filter/filter_numeric_field';

  createFilterNumericField(filterNumericField: Partial<modelFilterNumericField>): Observable<modelFilterNumericField> {
    return this.api.post<modelFilterNumericField>(this.endpoint, filterNumericField);
  }

}
