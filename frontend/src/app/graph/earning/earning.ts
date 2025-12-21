import { Component } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';
import { RetrieveEarningEstimate } from '../../services/retrieve-earning-estimate';
import { RetrieveEarningComp } from '../../components/retrieve-earning-comp/retrieve-earning-comp';
import { Earning } from '../../model/earning.type';


import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

@Component({
  selector: 'app-earning',
  imports: [],
  templateUrl: './earning.html',
  styleUrl: './earning.scss'
})
export class AppComponent {
public chart: any;

constructor(private service: RetrieveEarningEstimate){}


ngOnInit(): void {
    this.loadEarnings();
  }

  private loadEarnings(): void {
    this.service.getEarningFromApi().subscribe({
      next: (earnings: Earning[]) => {
        this.createChart(earnings);
      },
      error: (error) => {
        console.error('Error loading earnings data', error);
      }
    });
  }

  private createChart(earnings: Earning[]): void {
    const labels = earnings.map(e => e.period);   // adjust field name
    const values = earnings.map(e => e.avg);   // adjust field name

    this.chart = new Chart('MyChart', {
      type: 'bar',
      data: {
        labels,
        datasets: [
          {
            label: 'Earnings Estimate',
            data: values,
            borderWidth: 1
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