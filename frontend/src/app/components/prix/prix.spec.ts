import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Prix } from './prix';

describe('Prix', () => {
  let component: Prix;
  let fixture: ComponentFixture<Prix>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Prix]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Prix);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
