import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AppService]
})
export class AppComponent implements OnInit {
  ledC: boolean;
  ledG: boolean;
  ledSDB: boolean;
  ledS: boolean;

  constructor(public service: AppService) {

  }
  ngOnInit() {
    this.initFront();
  }


  bedSwitch(): void {
    this.service.getData('http://192.168.1.16:5000/CLightSwitch').subscribe((data: any) => {
      this.ledC = data.status;
    });
  }
  carSwitch(): void {
    this.service.getData('http://192.168.1.16:5000/GLightSwitch').subscribe((data: any) => {
      this.ledG = data.status;
    });
  }
  bathSwitch(): void {
    this.service.getData('http://192.168.1.16:5000/SDBLightSwitch').subscribe((data: any) => {
      this.ledSDB = data.status;
    });
  }
  TVSwitch(): void {
    this.service.getData('http://192.168.1.16:5000/SLightSwitch').subscribe((data: any) => {
      this.ledS = data.status;
    });
  }

  initFront() {
    this.service.getAllStatus().subscribe((data: any) => {
      this.ledG = data.data[0].G;
      this.ledSDB = data.data[1].SDB;
      this.ledS = data.data[2].S;
      this.ledC = data.data[3].C;
    });
  }
}
