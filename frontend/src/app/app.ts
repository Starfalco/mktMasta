import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatInputModule } from '@angular/material/input';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UI } from './ui/ui';
import { Header } from './components/header/header';
import { TableBasicExample } from './components/table-basic-example/table-basic-example';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);




@Component({
  selector: 'app-root',
  imports: [RouterOutlet, UI, Header, ],
  template: 
  `<app-header/>
  <app-ui/>
    
  <main>
  <router-outlet/>
  </main>

  
  `,
  styleUrl: './app.scss'
})
export class App {
  protected title = 'visual';

  
  


}
