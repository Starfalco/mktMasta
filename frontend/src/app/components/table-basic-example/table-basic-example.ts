import {Component} from '@angular/core';
import { APIServiceService } from './api-service.service';
import { Earning } from '../../model/earning.type';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf



const ELEMENT_DATA: Earning[] = [
];

/**
 * @title Basic use of `<table mat-table>`
 */
@Component({
  selector: 'app-table',
  styleUrls: ['table-basic-example.scss'],
  templateUrl: 'table-basic-example.html',
    imports: [
    CommonModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule
  ],
})

export class TableBasicExample {
  displayedColumns: string[] = ['Ticker','period', 'avg', 'low', 'high','yearAgoEps', 'numberOfAnalysts', 'growth'];
  dataSource = new MatTableDataSource<Earning>();

    constructor(private service: APIServiceService) {
    this.service.getData().then((data: Earning[]) => {
      this.dataSource.data = data;

     
      this.dataSource.filterPredicate = (row: Earning, filter: string) => {
        return row.Ticker.toLowerCase().includes(filter);
      };
    });
  }

applyFilter(event: KeyboardEvent) {
  const input = event.target as HTMLInputElement;
  const filterValue = input.value.trim().toLowerCase();
  this.dataSource.filter = filterValue;
}
}
