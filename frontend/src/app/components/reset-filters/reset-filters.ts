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

  async openModal() {
    this.initCacheService.initCache().subscribe();
    await sleep(1000); // Wait for 1 second before reloading the page
    window.location.reload();
  }
}


function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}