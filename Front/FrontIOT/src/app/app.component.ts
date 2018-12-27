import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';
import { interval } from 'rxjs';

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
  servoG: boolean;
  tempSTR: string;
  tempColor: string;

  constructor(public service: AppService) {

  }
  ngOnInit() {
    this.initFront();
    this.initTemp();
    interval(5000).subscribe(x => this.initTemp());


  }

  initTemp(): void {
    this.service.getData('http://192.168.1.16:5000/GetTemp').subscribe((data: any) => {
      console.log(data);
      this.tempSTR = data.temperature + '°C';
      if (data.temperature < 24) {
        this.tempColor = '#4a90e2';
      } else if (data.temperature < 30) {
        this.tempColor = '#add8bc';
      } else {
        this.tempColor = '#e13438';
      }
    });
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
  WarehouseSwitch(): void {
    this.service.getData('http://192.168.1.16:5000/WareHouseSwitch').subscribe((data: any) => {
      this.servoG = data.status;
    });
  }

  initFront() {
    this.service.getAllStatus().subscribe((data: any) => {
      this.ledG = data.data[0].G;
      this.ledSDB = data.data[1].SDB;
      this.ledS = data.data[2].S;
      this.ledC = data.data[3].C;
      this.servoG = data.data[4].W;
    });
  }
}
