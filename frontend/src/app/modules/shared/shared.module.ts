import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../style/material.module';
import { LayoutModule } from '@angular/cdk/layout';

const SHARED_MODULES = [
  // It may make sense to create another module and imports/exports all of Material module into one
  // we will keep it now simple
  MaterialModule,
  NgbModule,
  HttpClientModule,
  FormsModule,
  ReactiveFormsModule,
  LayoutModule,
];

const SHARED_COMPONENTS = [];

@NgModule({
  imports: [
    CommonModule,
    ...SHARED_MODULES,
  ],
  declarations: [
    ...SHARED_COMPONENTS
  ],
  exports: [
    ...SHARED_MODULES,
    ...SHARED_COMPONENTS
  ],
})
export class SharedModule { }
