import { Component } from '@angular/core';
import {InitCacheService} from "../../services/init-cache.service";

@Component({
  selector: 'app-reset-filters',
  imports: [],
  templateUrl: './reset-filters.html',
  styleUrl: './reset-filters.css',
})
export class ResetFilters {
  constructor(private initCacheService: InitCacheService) {}

  openModal() {
    this.initCacheService.initCache().subscribe();
    window.location.reload();
  }
}
