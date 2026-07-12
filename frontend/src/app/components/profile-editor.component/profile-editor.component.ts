import { Component, inject } from '@angular/core';
import {FormBuilder, ReactiveFormsModule} from '@angular/forms';
import {FilterStringField} from '../filter-string-field/filter-string-field';

@Component({
  selector: 'app-profile-editor',
  templateUrl: './profile-editor.component.html',
  styleUrls: ['./profile-editor.component.css'],
  imports: [ReactiveFormsModule],
})
export class ProfileEditorComponent {
  private filterStringField = inject(FilterStringField);
  private formBuilder = inject(FormBuilder);
  profileForm = this.formBuilder.group({
    filter: this.formBuilder.group({
      field: [''],
      contains: [''],
    }),
    aliases: this.formBuilder.array([this.formBuilder.control('')]),
  });
  updateProfile() {
    const { field, contains } = this.profileForm.get('filter')?.value || {};
    this.filterStringField.runFilterStringField(field || undefined, contains || undefined);
  };
}