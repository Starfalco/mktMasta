import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-headers',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './headers.html',
  styleUrl: './headers.css',
})
export class Headers {}