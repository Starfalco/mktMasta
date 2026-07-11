import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    pathMatch: 'full',
        loadComponent: () =>
      import('./main/main')
        .then(m => m.Main)
  },
  {
    path: 'screener',
    loadComponent: () =>
      import('./components/screener/screener')
        .then(m => m.Screener)
  },
  {
    path: 'filter-string-field',
    loadComponent: () =>
      import('./components/filter-string-field/filter-string-field')
        .then(m => m.FilterStringField)
  },
];