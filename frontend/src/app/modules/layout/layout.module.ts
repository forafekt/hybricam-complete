import { NgModule } from '@angular/core';

import { SharedModule } from '../shared/shared.module';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { NavigationComponent } from './navigation/navigation.component';
import { AboutComponent } from './about/about.component';
import { ServicesComponent } from './services/services.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { PricingComponent } from './pricing/pricing.component';
import { TestimonialComponent } from './testimonial/testimonial.component';
import { BrandComponent } from './brand/brand.component';
import { BlogComponent } from './blog/blog.component';

import { LoaderComponent } from './loader/loader.component';

// forms
import { SubscribeComponent } from './forms/subscribe/subscribe.component';
import { ContactComponent } from './forms/contact/contact.component';
import { CommonModule } from '@angular/common';


@NgModule({
  imports: [
    CommonModule,
    SharedModule,
  ],
  declarations: [
    HeaderComponent,
    FooterComponent,
    NavigationComponent,
    AboutComponent,
    ServicesComponent,
    PortfolioComponent,
    PricingComponent,
    TestimonialComponent,
    BrandComponent,
    BlogComponent,
    ContactComponent,
    LoaderComponent,
    SubscribeComponent,
  ],
  exports: [
    HeaderComponent,
    FooterComponent,
    NavigationComponent,
    AboutComponent,
    ServicesComponent,
    PortfolioComponent,
    PricingComponent,
    TestimonialComponent,
    BrandComponent,
    BlogComponent,
    ContactComponent,
    LoaderComponent,
    SubscribeComponent,
  ]
})
export class LayoutModule { }
