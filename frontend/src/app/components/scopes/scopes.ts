import { Component,inject, OnInit, signal } from '@angular/core';
import { scopes } from '../../model/scopesMod.type';
import { RetrieveScope } from '../../services/retrieve-scope';
import { MatTableModule } from '@angular/material/table';
import { MatTableDataSource } from '@angular/material/table';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { CommonModule } from '@angular/common'; // required for *ngFor, *ngIf 
import { catchError, BehaviorSubject, Observable } from 'rxjs';
import {CdkTableModule} from '@angular/cdk/table';
import {DataSource} from '@angular/cdk/collections';
import { MatSelectModule } from '@angular/material/select';




@Component({
  selector: 'app-scopes',
  imports: [
    CommonModule,
    MatTableModule,
    MatInputModule,
    MatFormFieldModule,
    MatSelectModule
  ],
  templateUrl: './scopes.html',

  styleUrl: './scopes.scss'
})

export class RetrieveScopes implements OnInit{
  retrieveScopes = inject(RetrieveScope);
  ScopesItems = signal<Array<scopes>>([]);
 

 ngOnInit(): void {
    this.retrieveScopes.getScopesFromApi()
    .pipe(
      catchError((err)=> {
        console.log(err);
        throw err;
      })
    ).subscribe((scopes) => {
      this.ScopesItems.set(scopes);
    });
 }

  onScopeChange(symbol: string): void {
  this.retrieveScopes.getDataBySymbol(symbol).subscribe();
}}