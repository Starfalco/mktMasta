import { TestBed } from '@angular/core/testing';

import { Initcache } from './init-cache';
import { init}

describe('InitCache', () => {
  let service: modelInitCache;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(modelInitCachesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
