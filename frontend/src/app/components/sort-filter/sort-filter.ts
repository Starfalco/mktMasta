import { Component, Injectable } from '@angular/core';
import { SortByFieldsService } from '../../services/sort-by-fields.service';


@Component({
  selector: 'app-sort-filter',
  imports: [],
  templateUrl: './sort-filter.html',
  styleUrl: './sort-filter.css',
})
@Injectable({
  providedIn: 'root',
})
export class SortFilter {


  constructor(
    private service: SortByFieldsService
  ) {
    this.runSortByField();
  }



  public runSortByField(
    field: string = '',
    ascending: boolean = true
  ): void {


    this.service
      .sortByField(
        field,
        ascending
      )
      .subscribe({

        next: data => {

          console.log(
            'SORT DATA:',
            data
          );

        },


        error: err => {

          console.error(
            'SORT ERROR:',
            err
          );

        }

      });

  }

}