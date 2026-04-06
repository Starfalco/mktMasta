import { TestBed } from '@angular/core/testing';

import { FilterStringFieldService } from './filter-string-field.service';

describe('FilterStringFieldService', () => {
  let service: FilterStringFieldService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FilterStringFieldService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
