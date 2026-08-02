import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';

import { DropdownComponent } from '../dropdown/dropdown';
import { SortFilter } from '../sort-filter/sort-filter';

import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';
import type { RetrieveCacheModel } from '../../model/retrieve-cache.model';

import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';


@Component({
  selector: 'app-filter-sort-form',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    DropdownComponent,
    CommonModule,
    MatFormFieldModule,
    MatSelectModule
  ],
  templateUrl: './filter-sort-form.html',
  styleUrls: ['./filter-sort-form.css'],
})
export class FilterSortForm {


  readonly displayedColumns: ScreenerColumn[] = screenerColumns;


  private formBuilder = inject(FormBuilder);

  private sortFilter = inject(SortFilter);



  profileForm = this.formBuilder.group({

    sort: this.formBuilder.group({

      field: [''],

      ascending: [true]

    })

  });



  private resolveFieldKey(
    fieldValue: string | null | undefined
  ): keyof RetrieveCacheModel | undefined {


    if (!fieldValue) {
      return undefined;
    }


    return this.displayedColumns.find(column =>
      column.key === fieldValue ||
      column.label === fieldValue
    )?.key;

  }



  async updateSort(): Promise<void> {


    const sortGroup = this.profileForm.get('sort');


    const fieldValue =
      sortGroup?.get('field')?.value ?? '';


    const ascending =
      sortGroup?.get('ascending')?.value ?? true;


    const fieldKey =
      this.resolveFieldKey(fieldValue);



    this.sortFilter.runSortByField(
      fieldKey ?? '',
      ascending
    );
    await sleep(1000); // Wait for 1 second before reloading the page
    window.location.reload();
  }
}

function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}







