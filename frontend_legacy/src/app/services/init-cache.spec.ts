import { TestBed } from '@angular/core/testing';

import { InitCache } from './init-cache';

describe('InitCache', () => {
  let service: InitCache;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InitCache);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
