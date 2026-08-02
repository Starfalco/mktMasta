import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SortOverlay } from './sort-overlay';

describe('SortOverlay', () => {
  let component: SortOverlay;
  let fixture: ComponentFixture<SortOverlay>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SortOverlay],
    }).compileComponents();

    fixture = TestBed.createComponent(SortOverlay);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
