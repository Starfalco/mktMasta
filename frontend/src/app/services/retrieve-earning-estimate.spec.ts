import { TestBed } from '@angular/core/testing';

import { RetrieveEarningEstimate } from './retrieve-earning-estimate';

describe('RetrieveEarningEstimate', () => {
  let service: RetrieveEarningEstimate;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RetrieveEarningEstimate);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
