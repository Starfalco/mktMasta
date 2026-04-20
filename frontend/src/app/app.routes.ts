import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'screener',
        loadComponent: () =>
            import('./components/screener/screener')
                .then(m => m.Screener)
    }]