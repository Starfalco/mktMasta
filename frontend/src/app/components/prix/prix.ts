import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatTableModule } from '@angular/material/table';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';

import { catchError } from 'rxjs';

import { scopes } from '../../model/scopesMod.type';
import { prices } from '../../model/prices';
import { RetrievePrix } from '../../services/prix';
import { RetrieveEarningEstimate } from '../../services/retrieve-earning-estimate';
import { Chart, registerables } from 'chart.js';
import { Earning } from '../../model/earning.type';
import { price } from '../../model/price.type';

@Component({
  selector: 'app-prix',
  standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatFormFieldModule,
    MatSelectModule
  ],
  templateUrl: './prix.html',
  styleUrls: ['./prix.scss']
})
export class RetrievePrixComponent implements OnInit {

  private prixService = inject(RetrievePrix);

  scopesItems = signal<scopes[]>([]);
  pricesItems = signal<prices[]>([]);
 
  

  displayedColumns: string[] = [
    'date', 'ticker', 'open', 'high', 'low', 'close', 'volume'
  ];

  private estimateService = inject(RetrievePrix);
  EarningEstItems = signal<Earning[]>([]);
  displayedColumnses: string[] = [  'estPeriod',
  'estAvg',
  'estLow',
  'estHigh',
  'estYearAgoEps',
  'estAnalysts',
  'estGrowth',
  'estTicker'];
  
  EarningHistItems = signal<price[]>([]);

  private chart?: Chart;

  ngOnInit(): void {
    this.loadScopes();
  }

  private loadScopes(): void {
    this.prixService.getScopesFromApi()
      .pipe(
        catchError(err => {
          console.error('Failed to load scopes', err);
          throw err;
        })
      )
      .subscribe(scopes => {
        this.scopesItems.set(scopes);
      });
  }

  onScopeChange(symbol: string): void {
  this.prixService.getPriceBySymbol(symbol).subscribe(prices => {
    this.pricesItems.set(prices);
    this.createChart(prices);
  });

  // Earnings table
  this.estimateService.getEarningEstBySymbol(symbol)
    .subscribe(Earning => {
      this.EarningEstItems.set(Earning);
      this.createChart2(Earning);

   });  
   
  }
  private createChart(prices: prices[]): void {
    const labels = prices.map(p => p.Date);
    const values = prices.map(p => p.Close);

  


    this.chart = new Chart('MyChart', {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: 'Close Price',
            data: values,
            borderWidth: 1,
            borderColor: '#FF6384',
            
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    })};
  private createChart2(history: Earning[]): void {
    const labels = history.map(p => p.period);
    const values = history.map(p => p.avg);

    
  
    this.chart = new Chart('MyChart1', {
      type: 'bar',
      data: {
        labels,
        datasets: [
          {
            label: 'History',
            data: values,
            borderWidth: 1,
            borderColor: '#FF6384',
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });    
  }
}