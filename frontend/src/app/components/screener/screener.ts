import {Component} from '@angular/core';
import { RetrieveCacheModel } from '../../model/retrieve-cache.model';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import { RetrieveCachesService } from '../../services/retrieve-cache.service';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf

@Component({
  selector: 'app-screener',
   standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule],
  templateUrl: './screener.html',
  styleUrl: './screener.css',
})
export class Screener {
  displayedColumns: string[] = ['sector',
    'industry',
    'ticker',
    'earnings_f0',
    'earnings_f1',
    'earnings_f2',
    'growth_f1',
    'growth_f2',
    'pe_f0',
    'pe_f1',
    'pe_f2',
    'peg_f1',
    'peg_f2',
    'surprise_average',
    'nb_analysts_f1',
    'nb_analysts_f2',
    'high_to_low_eps_f1',
    'high_to_low_eps_f2',
    'fiscal_month',
    'volatility',
    'max_drawn_down',
    'occurrence',
    'max_price',
    'earnings_f0_industry_bench',
    'earnings_f1_industry_bench',
    'earnings_f2_industry_bench',
    'earnings_f0_sector_bench',
    'earnings_f1_sector_bench',
    'earnings_f2_sector_bench',
    'earnings_f0_delta_industry',
    'earnings_f1_delta_industry',
    'earnings_f2_delta_industry',
    'earnings_f0_delta_sector',
    'earnings_f1_delta_sector',
    'earnings_f2_delta_sector',
    'growth_f1_industry_bench',
    'growth_f2_industry_bench',
    'growth_f1_sector_bench',
    'growth_f2_sector_bench',
    'growth_f1_delta_industry',
    'growth_f2_delta_industry',
    'growth_f1_delta_sector',
    'growth_f2_delta_sector',
    'pe_f0_industry_bench',
    'pe_f1_industry_bench',
    'pe_f2_industry_bench',
    'pe_f0_sector_bench',
    'pe_f1_sector_bench',
    'pe_f2_sector_bench',
    'pe_f0_delta_industry',
    'pe_f1_delta_industry',
    'pe_f2_delta_industry',
    'pe_f0_delta_sector',
    'pe_f1_delta_sector',
    'pe_f2_delta_sector',
    'pe_f1_vs_f0',
    'pe_f2_vs_f1',
    'scoring_f0',
    'scoring_f1',
    'scoring_f2',
    'surprise_average_industry_bench',
    'surprise_average_sector_bench'
  ];

  dataSource = new MatTableDataSource<RetrieveCacheModel>();
  constructor(private service: RetrieveCachesService) {
    this.service.getRetrieveCache().subscribe({
      next: data => {
        this.dataSource.data = data;
      },
      error: err => {
        console.error(err);
      }
    });
  }
}
