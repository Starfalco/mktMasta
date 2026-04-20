import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Screener } from './components/screener/screener';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,Screener],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = signal('frontend');
}