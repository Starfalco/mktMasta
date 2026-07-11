import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterStringField } from './filter-string-field';

describe('FilterStringField', () => {
  let component: FilterStringField;
  let fixture: ComponentFixture<FilterStringField>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FilterStringField],
    }).compileComponents();

    fixture = TestBed.createComponent(FilterStringField);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
