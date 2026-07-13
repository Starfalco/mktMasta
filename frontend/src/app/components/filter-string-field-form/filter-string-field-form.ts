import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { FilterStringField } from '../filter-string-field/filter-string-field';
import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';
import type { RetrieveCacheModel } from '../../model/retrieve-cache.model';

@Component({
  selector: 'app-filter-string-field-form',
  templateUrl: './filter-string-field-form.html',
  styleUrls: ['./filter-string-field-form.css'],
  imports: [ReactiveFormsModule],
})
export class FilterStringFieldFormComponent {
  readonly displayedColumns: ScreenerColumn[] = screenerColumns;
  private filterStringField = inject(FilterStringField);
  private formBuilder = inject(FormBuilder);

  profileForm = this.formBuilder.group({
    filter: this.formBuilder.group({
      field: [''],
      contains: [''],
    }),
    aliases: this.formBuilder.array([this.formBuilder.control('')]),
  });

  private resolveFieldKey(fieldValue: string | null | undefined): keyof RetrieveCacheModel | undefined {
    if (!fieldValue) {
      return undefined;
    }

    return this.displayedColumns.find(column =>
      column.key === fieldValue ||
      column.label === fieldValue
    )?.key;
  }

  updateProfile() {
    const filterGroup = this.profileForm.get('filter');
    const fieldValue = filterGroup?.get('field')?.value as string | null;
    const containsValue = filterGroup?.get('contains')?.value as string | null;
    const fieldKey = this.resolveFieldKey(fieldValue);

    this.filterStringField.runFilterStringField(fieldKey ?? '', containsValue ?? '');

    window.location.reload();
  }
}