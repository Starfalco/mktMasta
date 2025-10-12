import { Component, inject, OnInit, signal  } from '@angular/core';
import { Earning } from '../../model/earning.type';
import { RetrieveEarningEstimate } from '../../services/retrieve-earning-estimate';
import { catchError, BehaviorSubject, Observable } from 'rxjs';
import {CdkTableModule} from '@angular/cdk/table';
import {DataSource} from '@angular/cdk/collections';



@Component({
  selector: 'app-retrieve-earning-comp',
  imports: [],
  templateUrl: './retrieve-earning-estimate.html',
  styleUrl: './retrieve-earning-estimate.scss'
})





export class RetrieveEarningComp implements OnInit{
  retrieveEstimate = inject(RetrieveEarningEstimate);
  EarningItems = signal<Array<Earning>>([]);
 

  ngOnInit(): void {
    this.retrieveEstimate.getEarningFromApi()
    .pipe(
      catchError((err)=> {
        console.log(err);
        throw err;
      })
    ).subscribe((Earning) => {
      this.EarningItems.set(Earning);
    });
  }
}
