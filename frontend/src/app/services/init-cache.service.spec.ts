import { TestBed } from '@angular/core/testing';

import { InitCacheService } from './init-cache.service';

describe('InitCacheService', () => {
  let service: InitCacheService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InitCacheService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
