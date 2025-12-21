import { Component } from '@angular/core';
import { RetrieveScopes } from "../components/scopes/scopes";


@Component({
  selector: 'app-ui',
  imports: [RetrieveScopes],
  templateUrl: './ui.html',
  styleUrl: './ui.scss'
})
export class UI {

}
