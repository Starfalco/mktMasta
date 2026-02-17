import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EarningDates } from './earning-dates';

describe('EarningDates', () => {
  let component: EarningDates;
  let fixture: ComponentFixture<EarningDates>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EarningDates]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EarningDates);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
