import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterSortForm } from './filter-sort-form';

describe('FilterSortForm', () => {
  let component: FilterSortForm;
  let fixture: ComponentFixture<FilterSortForm>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FilterSortForm],
    }).compileComponents();

    fixture = TestBed.createComponent(FilterSortForm);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
