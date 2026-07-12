import { Component, Injectable } from '@angular/core';
import { HttpParams } from '@angular/common/http';
import { FilterStringFieldService } from '../../services/filter-string-field.service';

@Component({
  selector: 'app-filter-string-field',
  imports: [],
  templateUrl: './filter-string-field.html',
  styleUrl: './filter-string-field.css',
})
@Injectable({
  providedIn: 'root',
})
export class FilterStringField {
  constructor(private service: FilterStringFieldService) {
    this.runFilterStringField();
  }

  public runFilterStringField(field: string = '', contains: string = '', by_values: boolean = false): void {
    const params = new HttpParams()
      .set('field', field)
      .set('contains', contains)
      .set('by_values', by_values.toString());

    this.service.createFilterStringField(params).subscribe({
      next: data => {
        console.log('DATA:', data);
      },
      error: err => {
        console.error('ERROR:', err);
      }
    });
  }
}