import { TestBed } from '@angular/core/testing';

import { EarningDateServe } from './earning-date-serve';

describe('EarningDateServe', () => {
  let service: EarningDateServe;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EarningDateServe);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
