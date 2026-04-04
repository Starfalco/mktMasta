import { TestBed } from '@angular/core/testing';

import { Backendapi } from '../backendapi';

describe('Backendapi', () => {
  let service: Backendapi;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Backendapi);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
