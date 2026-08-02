import { Component, viewChild, DestroyRef, inject } from '@angular/core';

import { Overlay } from '@angular/cdk/overlay';
import { CdkPortal, PortalModule } from '@angular/cdk/portal';

import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

import {FilterSortForm} from '../filter-sort-form/filter-sort-form';


@Component({
  selector: 'app-sort-overlay',
  standalone: true,
  imports: [
    FilterSortForm,
    PortalModule
  ],
  templateUrl: './sort-overlay.html',
  styleUrl: './sort-overlay.css',
})
export class SortOverlay {


  portal = viewChild.required(CdkPortal);


  private overlay = inject(Overlay);

  private destroyRef = inject(DestroyRef);



  openModal() {


    const overlayRef = this.overlay.create({

      hasBackdrop: true,

      width: '60%',

      positionStrategy: this.overlay
        .position()
        .global()
        .centerHorizontally()
        .centerVertically(),

    });



    overlayRef.attach(this.portal());



    overlayRef.backdropClick()

      .pipe(
        takeUntilDestroyed(this.destroyRef)
      )

      .subscribe(() => {

        overlayRef.dispose();

      });

  }

}