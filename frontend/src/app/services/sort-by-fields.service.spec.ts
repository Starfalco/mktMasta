import { TestBed } from '@angular/core/testing';

import { SortByFieldsService } from './sort-by-fields.service';

describe('SortByFieldsService', () => {
  let service: SortByFieldsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SortByFieldsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
