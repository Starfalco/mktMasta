import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { FilterStringField } from '../filter-string-field/filter-string-field';
import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';
import type { RetrieveCacheModel } from '../../model/retrieve-cache.model';
import { DropdownComponent } from '../dropdown/dropdown';
import { ContainFieldService } from '../../services/contain-field-service';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
@Component({
  selector: 'app-filter-string-field-form',
  templateUrl: './filter-string-field-form.html',
  styleUrls: ['./filter-string-field-form.css'],
  imports: [ReactiveFormsModule, DropdownComponent, CommonModule,
  ReactiveFormsModule, DropdownComponent, MatFormFieldModule, MatSelectModule],
})
export class FilterStringFieldFormComponent {
  readonly displayedColumns: ScreenerColumn[] = screenerColumns;
  private filterStringField = inject(FilterStringField);
  private formBuilder = inject(FormBuilder);
  private containFieldService = inject(ContainFieldService);

  containsOptions: string[] = [];

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
constructor() {
  this.profileForm.get('filter.field')?.valueChanges.subscribe(field => {

    if (!field) {
      this.containsOptions = [];
      return;
    }

    this.containFieldService.createContainField(field).subscribe(data => {
      this.containsOptions = data;
    });

  });
}
  async updateProfile() {
    const filterGroup = this.profileForm.get('filter');
    const fieldValue = filterGroup?.get('field')?.value as string | null;
    const containsValue = filterGroup?.get('contains')?.value as string | null;
    const fieldKey = this.resolveFieldKey(fieldValue);

    this.filterStringField.runFilterStringField(fieldKey ?? '', containsValue ?? '');
    await sleep(1000); // Wait for 1 second before reloading the page
    window.location.reload();
  }
}

function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
