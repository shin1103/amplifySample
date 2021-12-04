import { Injectable } from '@angular/core';

import { API } from 'aws-amplify';

@Injectable({
  providedIn: 'root'
})
export class MyserviceService {

  constructor() { 

  }

  getItems(): Promise<any> {
    return API.get('angularSampleAPI', '/items', null)
  }

}
