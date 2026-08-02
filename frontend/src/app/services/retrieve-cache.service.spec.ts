import { testBed } from '@angular/core/testing';

import { RetrieveCachesService } from './retrieve-cache.service';

describe('RetrieveCachesService', () => {
  let service: RetrieveCachesService;

  beforeEach(() => {
    testBed.configureTestingModule({});
    service = testBed.inject(RetrieveCachesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
