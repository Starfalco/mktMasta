import { Component } from '@angular/core';
import { price } from '../../model/price.type';
import { APIServiceService } from './api-service.service';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf 


const ELEMENT_DATA: price[] = [
];



@Component({
  selector: 'app-price',
  imports: [
    CommonModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule
  ],
  templateUrl: 'price.html',
  styleUrl: 'price.scss',
  

})
export class pricetable {
  displayedColumns: string[] = ['date','Ticker', 'epsActual','epsEstimate','epsDifference','surprisePercent'];
  dataSource = new MatTableDataSource<price>();

    constructor(private service: APIServiceService) {
    this.service.getData().then((data: price[]) => {
      this.dataSource.data = data;

      
      this.dataSource.filterPredicate = (row: price, filter: string) => {
        return row.Ticker.toLowerCase().includes(filter);
     };
    });
  }

applyFilter(event: KeyboardEvent) {
  const input = event.target as HTMLInputElement;
  const filterValue = input.value.trim().toLowerCase();
  this.dataSource.filter = ''; // Force clear first (optional workaround)
  this.dataSource.filter = filterValue;
}
}

