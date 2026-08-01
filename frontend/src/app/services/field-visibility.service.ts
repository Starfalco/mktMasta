import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { screenerColumns } from '../model/screener.model';

@Injectable({
  providedIn: 'root'
})
export class FieldVisibilityService {
  private storageKey = 'screener_visible_fields';

  private visibleFieldsSubject = new BehaviorSubject<string[]>(
    this.loadFromStorage() || screenerColumns.map(c => c.key)
  );

  visibleFields$ = this.visibleFieldsSubject.asObservable();

  getVisibleFields(): string[] {
    return this.visibleFieldsSubject.getValue();
  }

  toggleField(key: string) {
    const current = this.visibleFieldsSubject.getValue();
    const newFields = current.includes(key)
      ? current.filter(k => k !== key)
      : [...current, key];
    this.visibleFieldsSubject.next(newFields);
    this.saveToStorage(newFields);
  }

  private loadFromStorage(): string[] | null {
    const stored = localStorage.getItem(this.storageKey);
    return stored ? JSON.parse(stored) : null;
  }

  private saveToStorage(fields: string[]) {
    localStorage.setItem(this.storageKey, JSON.stringify(fields));
  }
}