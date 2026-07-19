import { Component } from '@angular/core';
import { RetrieveCacheModel } from '../../model/retrieve-cache.model';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import { RetrieveCachesService } from '../../services/retrieve-cache.service';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf
import { FilterOverlay } from '../overlay/overlay-components';
import {ResetFilters} from "../reset-filters/reset-filters";
import { PortalModule } from '@angular/cdk/portal';
import { screenerColumns, type ScreenerColumn } from '../../model/screener.model';

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
    PortalModule],
  templateUrl: './screener.html',
  styleUrl: './screener.css',
})

export class Screener {
  readonly displayedColumns: ScreenerColumn[] = screenerColumns;

  get displayedColumnKeys(): Array<keyof RetrieveCacheModel> {
    return this.displayedColumns.map(column => column.key);
  }

  dataSource = new MatTableDataSource<RetrieveCacheModel>();

  constructor(private service: RetrieveCachesService) {
    this.service.getRetrieveCache().subscribe({
      next: data => {
        console.log('DATA:', data);
        this.dataSource.data = data;
      },
      error: err => {
        console.error('ERROR:', err);
      }
    });
  }
}
