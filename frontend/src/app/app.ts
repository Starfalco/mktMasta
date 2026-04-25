import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Headers } from './headers/headers';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,Headers],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = signal('frontend');
}