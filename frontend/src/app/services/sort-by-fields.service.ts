import { inject, Injectable } from '@angular/core';
import { BackendApiService } from '../core/service/backend-api.service';
import { Observable } from 'rxjs';
import { SortByFieldsModel } from '../model/sort-by-fields.model';

@Injectable({
  providedIn: 'root',
})
export class SortByFieldsService {
  private api = inject(BackendApiService);

  private endpoint = 'sort/sort_by_fields';

  createSortByFields(sortByFields: Partial<SortByFieldsModel>): Observable<SortByFieldsModel> {
    return this.api.post<SortByFieldsModel>(this.endpoint, sortByFields);
  }
}
