import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TableBasicExample } from './table-basic-example';

describe('TableBasicExample', () => {
  let component: TableBasicExample;
  let fixture: ComponentFixture<TableBasicExample>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TableBasicExample]
      
    })
    .compileComponents();

    fixture = TestBed.createComponent(TableBasicExample);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
