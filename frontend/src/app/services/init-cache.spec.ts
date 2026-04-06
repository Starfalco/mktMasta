import { testBed } from '@angular/core/testing';

import { initCache } from './init-cache';
import { init }

describe('initCache', () => {
  let service: modelInitCache;

  beforeEach(() => {
    testBed.configureTestingModule({});
    service = testBed.inject(modelInitCachesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
