import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterStringFieldFormComponent } from './filter-string-field-form';

describe('FilterStringFieldFormComponent', () => {
  let component: FilterStringFieldFormComponent;
  let fixture: ComponentFixture<FilterStringFieldFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FilterStringFieldFormComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(FilterStringFieldFormComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
