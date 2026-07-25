import { Component, forwardRef } from '@angular/core';
import { CommonModule } from '@angular/common';

import {ControlValueAccessor, FormsModule,NG_VALUE_ACCESSOR} from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { FILTER_STRING_FIELD_OPTIONS } from '../../model/filter-string-field.model';

@Component({
  selector: 'app-dropdown',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatFormFieldModule,
    MatSelectModule
  ],
  templateUrl: './dropdown.html',
  styleUrls: ['./dropdown.css'],
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => DropdownComponent),
      multi: true
    }
  ]
})
export class DropdownComponent implements ControlValueAccessor {

  fieldOptions = FILTER_STRING_FIELD_OPTIONS;

  value = '';
  disabled = false;

  private onChange = (_: string) => {};
  private onTouched = () => {};

  writeValue(value: string): void {
    this.value = value ?? '';
  }

  registerOnChange(fn: (value: string) => void): void {
    this.onChange = fn;
  }

  registerOnTouched(fn: () => void): void {
    this.onTouched = fn;
  }

  setDisabledState(isDisabled: boolean): void {
    this.disabled = isDisabled;
  }

  valueChanged(value: string): void {
    this.value = value;
    this.onChange(value);
    this.onTouched();
  }
}