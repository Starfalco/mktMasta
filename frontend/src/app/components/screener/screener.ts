import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import { RetrieveCachesService } from '../../services/retrieve-cache.service';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FilterOverlay } from '../overlay/overlay-components';
import { ResetFilters } from "../reset-filters/reset-filters";
import { PortalModule } from '@angular/cdk/portal';
import { SortOverlay } from "../sort-overlay/sort-overlay";
import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';
import { RetrieveCacheModel } from '../../model/retrieve-cache.model';
import { FieldVisibilityService } from '../../services/field-visibility.service';
import { MatDialog } from '@angular/material/dialog';
import { FieldSelectorComponent } from '../field-selector/field-selector';

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
  styleUrl: './screener.css',
})
export class Screener implements OnInit {
  private fieldVisibilityService = inject(FieldVisibilityService);
  private dialog = inject(MatDialog);
  private service = inject(RetrieveCachesService);

  displayedColumns: ScreenerColumn[] = [];
  dataSource = new MatTableDataSource<RetrieveCacheModel>();

  ngOnInit() {
    this.service.getRetrieveCache().subscribe({
      next: data => {
        this.updateDisplayedColumns(data);
        this.dataSource.data = data;
      },
      error: err => {
        console.error('ERROR:', err);
      }
    });

    // Subscribe to visibility changes
    this.fieldVisibilityService.visibleFields$.subscribe(fields => {
      this.updateDisplayedColumnsBasedOnVisibility(fields);
    });
  }

  private updateDisplayedColumns(data: RetrieveCacheModel[]): void {
    const availableKeys = new Set<string>();
    data.forEach(item => {
      Object.keys(item).forEach(key => availableKeys.add(key));
    });

    // Filter by availability first
    const availableColumns = screenerColumns.filter(column =>
      availableKeys.has(column.key as string)
    );

    // Then filter by visibility
    this.updateDisplayedColumnsBasedOnVisibility(this.fieldVisibilityService.getVisibleFields(), availableColumns);
  }

  private updateDisplayedColumnsBasedOnVisibility(visibleKeys: string[], availableColumns?: ScreenerColumn[]) {
    const columnsToUse = availableColumns || screenerColumns;
    this.displayedColumns = columnsToUse.filter(column =>
      visibleKeys.includes(column.key)
    );
  }

  openFieldSelector() {
    this.dialog.open(FieldSelectorComponent);
  }

  get displayedColumnKeys(): Array<keyof RetrieveCacheModel> {
    return this.displayedColumns.map(column => column.key);
  }
}
