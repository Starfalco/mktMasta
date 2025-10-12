import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RetrieveEarningEstimate } from './retrieve-earning-comp';

describe('RetrieveEarningEstimate', () => {
  let component: RetrieveEarningEstimate;
  let fixture: ComponentFixture<RetrieveEarningEstimate>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RetrieveEarningEstimate]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RetrieveEarningEstimate);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
