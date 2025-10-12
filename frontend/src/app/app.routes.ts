import { Routes } from '@angular/router';

export const routes: Routes = [{
    path: 'earning',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./components/table-basic-example/table-basic-example').then((m)=>m.TableBasicExample)
    },
},
{
    path: 'ui',
    loadComponent:() => {
        return import('./ui/ui').then ((m)=>m.UI)
        
    },
},

{
    path: 'price',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./components/price/price').then((m)=>m.pricetable)
    },
},
];
