import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatButtonModule } from '@angular/material/button';
import { screenerColumns } from '../../model/screener.model';
import { FieldVisibilityService } from '../../services/field-visibility.service';

@Component({
  selector: 'app-field-selector',
  standalone: true,
  imports: [CommonModule, MatDialogModule, MatCheckboxModule, MatButtonModule],
  templateUrl: './field-selector.html',
  styleUrls: ['./field-selector.css']
})
export class FieldSelectorComponent {
  private dialogRef = inject(MatDialogRef<FieldSelectorComponent>);
  private fieldVisibilityService = inject(FieldVisibilityService);

  columns = screenerColumns;

  isVisible(key: string): boolean {
    return this.fieldVisibilityService.getVisibleFields().includes(key);
  }

  toggle(key: string) {
    this.fieldVisibilityService.toggleField(key);
  }

  close() {
    this.dialogRef.close();
  }
}