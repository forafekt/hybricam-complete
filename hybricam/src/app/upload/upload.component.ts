import { Component, OnInit, ViewChild } from '@angular/core';

import { CameraComponent } from '../camera/camera.component';


@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {

  selectedFilter = '';
  selectedIndex = 0;
  result: HTMLElement;

  stream: any = '';
  
  slideOpts = {
    slidesPerView: 3.5,
    spaceBetween: 5,
    slidesOffsetBefore: 20,
    freeMode: true
  };
 
  filterOptions = [
    { name: 'Normal', value: '' },
    { name: 'Sepia', value: 'sepia' },
    { name: 'Blue Monotone', value: 'blue_monotone' },
    { name: 'Violent Tomato', value: 'violent_tomato' },
    { name: 'Grey', value: 'greyscale' },
    { name: 'Brightness', value: 'brightness' },
    { name: 'Saturation', value: 'saturation' },
    { name: 'Contrast', value: 'contrast' },
    { name: 'Hue', value: 'hue' },
    { name: 'Cookie', value: 'cookie' },
    { name: 'Vintage', value: 'vintage' },
    { name: 'Koda', value: 'koda' },
    { name: 'Technicolor', value: 'technicolor' },
    { name: 'Polaroid', value: 'polaroid' },
    { name: 'Bgr', value: 'bgr' }
  ];

  async selectImage() {
    const stream = CameraComponent 
    this.stream = stream;
  }

  filter(index: number) {
    this.selectedFilter = this.filterOptions[index].value;
    this.selectedIndex = index;
  }
 
  imageLoaded(e: { detail: { result: HTMLElement; }; }) {
    // Grab a reference to the canvas/image
    this.result = e.detail.result;
  }
 
  saveImage() {
    let base64 = '';
    if (!this.selectedFilter) {
      // Use the original image!
      base64 = this.stream.data;
    } else {
      let canvas = this.result as HTMLCanvasElement;
      // export as dataUrl or Blob!
      base64 = canvas.toDataURL('image/jpeg', 1.0);
    }
 
    // Do whatever you want with the result, e.g. download on desktop
    this.downloadBase64File(base64);
  }
 
  // https://stackoverflow.com/questions/16996319/javascript-save-base64-string-as-file
  downloadBase64File(base64: string) {
    const linkSource = `${base64}`;
    const downloadLink = document.createElement('a');
    document.body.appendChild(downloadLink);
 
    downloadLink.href = linkSource;
    downloadLink.target = '_self';
    downloadLink.download = 'test.png';
    downloadLink.click();
  }

  @ViewChild('appCamera') appCamera: CameraComponent;
  hiddenCamera: boolean = true;

  nativeApproach: boolean = false;

  

  constructor() { }

  ngOnInit() {
  
  }

  changeApproachType(){
    this.nativeApproach = !this.nativeApproach;
  }

  triggerCamera() {
    let input = document.getElementById('capture');
    input.click();
  }

  onImageUpdate(event: { target: { files: any[]; }; }){
    const file = event.target.files[0];
    console.log('Name: '+file.name);
    console.log('Size: '+file.size/Math.pow(1024,2)+' mb');
  }

  openCamera(): void {
    this.appCamera.initCamera();
    this.hiddenCamera = false;
  }
  
  loadCaptureStream(stream: any): void {
    this.hiddenCamera = true;
    this.stream = stream;
  }
}