import { Component } from '@angular/core';
import { MyserviceService } from './myservice.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-amplify-pc';
  message = null

  constructor(myservice: MyserviceService){
    myservice.getItems().then( (result) => {
      this.message = result
    })
  }
  
}
