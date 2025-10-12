import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UI } from './ui';

describe('UI', () => {
  let component: UI;
  let fixture: ComponentFixture<UI>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UI]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UI);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
