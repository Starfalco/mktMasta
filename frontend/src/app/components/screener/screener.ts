import {
  Component,
  OnInit,
  AfterViewInit,
  ViewChild,
  ChangeDetectorRef,
  inject
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule, MatTable, MatTableDataSource } from '@angular/material/table';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatDialog } from '@angular/material/dialog';
import { PortalModule } from '@angular/cdk/portal';

import { RetrieveCachesService } from '../../services/retrieve-cache.service';
import { FieldVisibilityService } from '../../services/field-visibility.service';

import { FilterOverlay } from '../overlay/overlay-components';
import { ResetFilters } from '../reset-filters/reset-filters';
import { SortOverlay } from '../sort-overlay/sort-overlay';
import { FieldSelectorComponent } from '../field-selector/field-selector';

import {
  screenerColumns,
  ScreenerColumn
} from '../../model/screener.model';

import { RetrieveCacheModel } from '../../model/retrieve-cache.model';

@Component({
  selector: 'app-screener',
  standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule,
    FilterOverlay,
    ResetFilters,
    PortalModule,
    SortOverlay
  ],
  templateUrl: './screener.html',
  styleUrl: './screener.css'
})
export class Screener implements OnInit, AfterViewInit {

  private service = inject(RetrieveCachesService);
  private dialog = inject(MatDialog);
  private fieldVisibilityService = inject(FieldVisibilityService);
  private cdr = inject(ChangeDetectorRef);

  @ViewChild(MatTable)
  table?: MatTable<RetrieveCacheModel>;

  dataSource = new MatTableDataSource<RetrieveCacheModel>();

  displayedColumns: ScreenerColumn[] = [];

  private availableColumns: ScreenerColumn[] = [];

  ngOnInit(): void {

    this.service.getRetrieveCache().subscribe({
      next: data => {

        this.dataSource.data = data;

        const availableKeys = new Set<string>();

        data.forEach(item => {
          Object.keys(item).forEach(key => availableKeys.add(key));
        });

        this.availableColumns = screenerColumns.filter(column =>
          availableKeys.has(column.key)
        );

        this.updateDisplayedColumns(
          this.fieldVisibilityService.getVisibleFields()
        );
      },
      error: err => console.error(err)
    });

  }

  ngAfterViewInit(): void {

    this.fieldVisibilityService.visibleFields$.subscribe(fields => {

      console.log('Visible fields:', fields);

      this.updateDisplayedColumns(fields);

      this.cdr.detectChanges();

    });

  }

  private updateDisplayedColumns(visibleFields: string[]): void {

    this.displayedColumns = this.availableColumns.filter(column =>
      visibleFields.includes(column.key)
    );

    console.log('Displayed columns:', this.displayedColumns);

    this.table?.renderRows();
  }
  // formatValue(value: unknown): string {
  // if (typeof value === 'number') {
  //   return value.toFixed(2);
  // }

  // return value?.toString() ?? '';
// formatValue(value: unknown): unknown {
//   return value;
// }
  isNumber(value: unknown): boolean {
  return typeof value === 'number';
}
  openFieldSelector(): void {
    this.dialog.open(FieldSelectorComponent);
  }

  get displayedColumnKeys(): Array<keyof RetrieveCacheModel> {
    return this.displayedColumns.map(column => column.key);
  }

}