import { TestBed } from '@angular/core/testing';

import { retrievecache}

describe('InitRetrieve', () => {
  let service: InitRetrieve;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InitRetrieve);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
