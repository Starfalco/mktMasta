import { Component } from '@angular/core';
import { RetrieveCacheModel } from '../../model/retrieve-cache.model';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import { RetrieveCachesService } from '../../services/retrieve-cache.service';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf
import { FilterOverlay } from '../overlay/overlay-components';
import { ResetFilters } from "../reset-filters/reset-filters";
import { PortalModule } from '@angular/cdk/portal';
import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';
import { SortOverlay } from "../sort-overlay/sort-overlay";


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

export class Screener {
  displayedColumns: ScreenerColumn[] = screenerColumns;

  get displayedColumnKeys(): Array<keyof RetrieveCacheModel> {
    return this.displayedColumns.map(column => column.key);
  }

  dataSource = new MatTableDataSource<RetrieveCacheModel>();

  constructor(private service: RetrieveCachesService) {
    this.service.getRetrieveCache().subscribe({
      next: data => {
        this.updateDisplayedColumns(data);
        this.dataSource.data = data;
      },
      error: err => {
        console.error('ERROR:', err);
      }
    });
  }

  private updateDisplayedColumns(data: RetrieveCacheModel[]): void {
    const availableKeys = new Set<string>();

    data.forEach(item => {
      Object.keys(item).forEach(key => availableKeys.add(key));
    });

    this.displayedColumns = screenerColumns.filter(column =>
      availableKeys.has(column.key as string)
    );
  }
}
