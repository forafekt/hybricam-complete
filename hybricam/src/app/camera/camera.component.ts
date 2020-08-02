import { Component, OnInit, Output, EventEmitter, ViewChild, ElementRef } from '@angular/core';

import DetectRTC from 'detectrtc';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.scss', './camera.scss']
})
export class CameraComponent implements OnInit {
  @ViewChild('stream') videoRef: ElementRef;
  @ViewChild('snapshot') canvasRef: ElementRef;
  @Output() capture = new EventEmitter();

  video: HTMLVideoElement;
  canvas: HTMLCanvasElement;

  viewingSnapshot: boolean = false;

  constructor( public snackBar: MatSnackBar) { }

  ngOnInit() {
  }

  public initCamera(): void {
    DetectRTC.load(() => {
      // Check if camera feature is supported
      if (DetectRTC.isWebRTCSupported == false) {
        alert('Please use Chrome, Firefox, iOS 11+, Android 5 or higher, Safari 11 or higher');
      } else {
        if (DetectRTC.hasWebcam == false) {
          alert('Please install an external webcam device.');
        } else {
          this.initCameraUI();
          this.clearSnapshot();
          this.initCameraStream();
        }
      }
      console.log("RTC Debug info: " + 
        "\n OS:                   " + DetectRTC.osName + " " + DetectRTC.osVersion + 
        "\n browser:              " + DetectRTC.browser.fullVersion + " " + DetectRTC.browser.name +
        "\n is Mobile Device:     " + DetectRTC.isMobileDevice +
        "\n has webcam:           " + DetectRTC.hasWebcam + 
        "\n has permission:       " + DetectRTC.isWebsiteHasWebcamPermission +       
        "\n getUserMedia Support: " + DetectRTC.isGetUserMediaSupported + 
        "\n isWebRTC Supported:   " + DetectRTC.isWebRTCSupported + 
        "\n WebAudio Supported:   " + DetectRTC.isAudioContextSupported +
        "\n is Mobile Device:     " + DetectRTC.isMobileDevice+
        "\n Total amount of Cameras:     " + DetectRTC.videoInputDevices.length
      );
    });
  }

  initCameraUI(): void {
    this.video = this.videoRef.nativeElement;
    this.canvas = this.canvasRef.nativeElement;
  }

  initCameraStream() {
    // Stop any active streams in the window
    if (window['stream']) {
      window['stream'].getTracks().forEach((track: { stop: () => void; }) => {
        track.stop();
      });
    }

    let constraints = {
      audio: false,
      video: {
        width: { min: 1024, ideal: 1920, max: 3840 },
        height: { min: 576, ideal: 1080, max: 2160 },
        facingMode: { exact: 'environment' }
      }
    };

    console.log('video 1920')

    const handleSuccess = (stream: MediaProvider) => {
      window['stream'] = stream; // Make stream available to browser console
      this.video.srcObject = stream;
      return navigator.mediaDevices.enumerateDevices();
    }

    const handleError = (error: string) => {
      console.log('ERROR: '+error);
      if (error === 'PermissionDeniedError') {
        alert("Permission denied. Please refresh and give permission.");
      }
    }

    navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);
  }

  takeSnapshot(): void {
    console.log('VIDEO WIDTH: '+this.video.videoWidth+' VIDEO HEIGHT: '+this.video.videoHeight);

    this.canvas.width = this.video.videoWidth;
    this.canvas.height = this.video.videoHeight;

    this.canvas.getContext('2d').drawImage(this.video, 0, 0, this.video.videoWidth, this.video.videoHeight);

    this.viewingSnapshot = true;
  }

  retakeSnapshot(): void {
    this.clearSnapshot();
    this.viewingSnapshot = false;
  }

  clearSnapshot(): void {
    this.canvas.getContext("2d").clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.viewingSnapshot = false;
  }

  stopVideo(): void {
    if (window['stream']) {
      window['stream'].getTracks().forEach((track: { stop: () => void; }) => {
        track.stop();
      });
    }
  }

  confirmSnapshot(): void{
    let canvasResult: HTMLCanvasElement = document.createElement('canvas');

    const width = this.video.videoWidth*0.8;
    const height = this.video.videoHeight*0.35;

    console.log('width: '+width+' height: '+height);

    canvasResult.width = width;
    canvasResult.height = height;

    const left = this.video.videoWidth*0.085;
    const top = this.video.videoHeight*0.25;

    console.log('LEFT: '+left+' TOP: '+top);

    let imageData = this.canvas.getContext("2d").getImageData(left, top, width, height);

    let ctx = canvasResult.getContext("2d");
    ctx.rect(0, 0, width, height);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.putImageData(imageData, 0, 0);

    this.stopVideo();

    const getCanvasBlob = (canvas: HTMLCanvasElement) => {
      return new Promise(resolve => {
        canvas.toBlob(resolve, 'image/jpeg', 1.0);
      })
    };

    getCanvasBlob(canvasResult).then((blob: Blob) => {
      console.log('Size: '+blob.size/Math.pow(1024,2)+' mb');
      let blobResult = {
        os: DetectRTC.osName + " " + DetectRTC.osVersion,
        size: blob.size/Math.pow(1024,2)+' mb',
        browser: DetectRTC.browser.fullVersion + " " + DetectRTC.browser.name,
        resolution: DetectRTC.displayResolution,
        ratio: DetectRTC.displayAspectRatio,
        data: ''
      }
      // do something with the image blob
      let reader = new FileReader();
      reader.onload = (blobResult: any) => {
        console.log('Blob in Base64: '+reader.result);
        blobResult.data = reader.result;
        this.capture.emit(blobResult);
      };
      reader.readAsDataURL(blob); // converts the blob to base64 and calls onload
    });
  }

}