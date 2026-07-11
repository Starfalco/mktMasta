import { Component, inject } from '@angular/core';
import {FormBuilder, ReactiveFormsModule, Validators, FormArray} from '@angular/forms';
import {FilterStringField} from '../filter-string-field/filter-string-field';
import {FilterStringFieldService} from '../../services/filter-string-field.service';

@Component({
  selector: 'app-profile-editor',
  templateUrl: './profile-editor.component.html',
  styleUrls: ['./profile-editor.component.css'],
  imports: [ReactiveFormsModule],
})
export class ProfileEditorComponent {
  private filterStringField = inject(FilterStringFieldService);
  private formBuilder = inject(FormBuilder);
  profileForm = this.formBuilder.group({
    firstName: ['', Validators.required],
    lastName: [''],
    address: this.formBuilder.group({
      street: [''],
      city: [''],
      state: [''],
      zip: [''],
    }),
    aliases: this.formBuilder.array([this.formBuilder.control('')]),
  });
  updateProfile() {
    this.profileForm.patchValue({
      firstName: 'Nancy',
      address: {
        street: '123 Drew Street',
      },
    });
  };
  // updateProfile() {
  //   this.filterStringField.runFilterStringField();
  // };
  // get aliases() {
  //   return this.profileForm.get('aliases') as FormArray;
  // };
  // addAlias() {
  //   this.aliases.push(this.formBuilder.control(''));
  // };
}