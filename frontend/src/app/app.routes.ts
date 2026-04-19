import { Routes } from '@angular/router';

export const routes: Routes = [{
    path: 'screener',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./components/screener/screener').then((m)=>m.Screener)
    },
},
];