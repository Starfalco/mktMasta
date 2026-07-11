import { Component, model } from '@angular/core';
import { HttpParams } from '@angular/common/http';
import { FilterStringFieldModel } from '../../model/filter-string-field.model';
import { FilterStringFieldService } from '../../services/filter-string-field.service';

@Component({
  selector: 'app-filter-string-field',
  imports: [],
  templateUrl: './filter-string-field.html',
  styleUrl: './filter-string-field.css',
})
export class FilterStringField {
  constructor(private service: FilterStringFieldService) {
    this.runFilterStringField();
  }

  public runFilterStringField() {
    const params = new HttpParams()
      .set('field', 'sector')
      .set('contains', 'Technology')
      .set('by_values', 'false');

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