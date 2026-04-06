import { testBed } from '@angular/core/testing';

import { retrieveCache }

describe('retrieveCache', () => {
  let service: retrieveCache;

  beforeEach(() => {
    testBed.configureTestingModule({});
    service = testBed.inject(retrieveCache);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
