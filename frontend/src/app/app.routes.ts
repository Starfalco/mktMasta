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
{
    path: 'graph',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./graph/earning/earning').then((m)=>m.AppComponent)
    }
},
{
    path: 'scopes',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./components/scopes/scopes').then((m)=>m.RetrieveScopes)
    }
},
{
    path: 'Prix',
    pathMatch: 'full',
    loadComponent: () => {
        return import('./components/prix/prix').then((m)=>m.RetrievePrixComponent)
    }
}

];
