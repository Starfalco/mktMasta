import { Component } from '@angular/core';
import { NameEditorComponent } from '../name-editor.component/name-editor.component';
import { ProfileEditorComponent } from '../profile-editor.component/profile-editor.component';
import { inject } from '@angular/core';
import { Overlay } from '@angular/cdk/overlay';
import { CdkPortal, PortalModule } from '@angular/cdk/portal';
import { viewChild } from '@angular/core';
import { CdkOverlayOrigin } from '@angular/cdk/overlay';
import { OverlayConfig } from '@angular/cdk/overlay';

@Component({
  selector: 'app-overlay-components',
  imports: [  
    NameEditorComponent,
    ProfileEditorComponent,
    PortalModule,
  CdkOverlayOrigin],
  templateUrl: './overlay-components.html',
  styleUrl: './overlay-components.css',
})
export class FilterOverlay {
    protected detailsOpen = false;
    portal = viewChild.required<CdkPortal>(CdkPortal)

    private overlay = inject(Overlay);
    protected openModal() {
    const config = new OverlayConfig({
            positionStrategy: this.overlay.position().global().centerHorizontally().centerVertically(),
            width: '30%'
        });
        const overlayRef = this.overlay.create(config);
        overlayRef.attach(this.portal());
    }
}
