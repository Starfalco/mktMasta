import { Component } from '@angular/core';
import { FilterStringFieldFormComponent } from '../filter-string-field-form/filter-string-field-form';
import { Overlay } from '@angular/cdk/overlay';
import { CdkPortal, PortalModule, } from '@angular/cdk/portal';
import { viewChild, DestroyRef, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-overlay-components',
  imports: [
    FilterStringFieldFormComponent,
    PortalModule,],
  templateUrl: './overlay-components.html',
  styleUrl: './overlay-components.css',
})
export class FilterOverlay {

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
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(() => overlayRef.dispose());
  }
}