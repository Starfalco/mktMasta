import { TestBed } from '@angular/core/testing';

import { Prix } from './prix';

describe('Prix', () => {
  let service: Prix;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Prix);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
