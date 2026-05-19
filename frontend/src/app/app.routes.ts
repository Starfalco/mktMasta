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
    path: 'name-editor',
    loadComponent: () =>
      import('./components/name-editor.component/name-editor.component')
        .then(m => m.NameEditorComponent)
  },
  {
    path: 'profile-editor',
    loadComponent: () =>
      import('./components/profile-editor.component/profile-editor.component')
        .then(m => m.ProfileEditorComponent)
  }
];