import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';

import { App } from './app/app';
import { routes } from './app/app.routes';
import { ConfigService } from './app/services/config-file-service';

bootstrapApplication(App, {
  providers: [
    provideRouter(routes),
    provideHttpClient(withInterceptorsFromDi())
  ]
}).then(() => {
  // Load config from backend after bootstrap.
  // HttpClient is now available in DI, and ConfigService uses inject(HttpClient).
  // This is fine — most API calls happen after user interaction.
  const configService = new ConfigService();
  configService.loadConfig().catch(() => {
    console.warn('Config loading failed at startup. API calls will use fallback config.');
  });
});
