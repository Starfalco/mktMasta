import { TestBed } from '@angular/core/testing';

import { RetrieveScope } from './retrieve-scope';

describe('RetrieveScope', () => {
  let service: RetrieveScope;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RetrieveScope);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
