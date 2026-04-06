import { TestBed } from '@angular/core/testing';

import { FilterNumericField } from './filter-numeric-field';

describe('FilterNumericField', () => {
  let service: FilterNumericField;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FilterNumericField);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
