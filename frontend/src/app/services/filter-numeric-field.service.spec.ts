import { TestBed } from '@angular/core/testing';

import { FilterNumericFieldService } from './filter-numeric-field.service';

describe('FilterNumericFieldService', () => {
  let service: FilterNumericFieldService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FilterNumericFieldService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
