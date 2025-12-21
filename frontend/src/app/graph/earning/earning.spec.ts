import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Earning } from '.';

describe('Earning', () => {
  let component: Earning;
  let fixture: ComponentFixture<Earning>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Earning]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Earning);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
