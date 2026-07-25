import { TestBed } from '@angular/core/testing';

import { ContainFieldService } from './contain-field-service';

describe('ContainFieldService', () => {
  let service: ContainFieldService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ContainFieldService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
