import {NgModule} from '@angular/core';

import {NgbAccordionModule} from '@ng-bootstrap/ng-bootstrap/accordion/accordion.module';
import {NgbAlertModule} from '@ng-bootstrap/ng-bootstrap/alert/alert.module';
import {NgbButtonsModule} from '@ng-bootstrap/ng-bootstrap/buttons/buttons.module';
import {NgbCarouselModule} from '@ng-bootstrap/ng-bootstrap/carousel/carousel.module';
import {NgbCollapseModule} from '@ng-bootstrap/ng-bootstrap/collapse/collapse.module';
import {NgbDatepickerModule} from '@ng-bootstrap/ng-bootstrap/datepicker/datepicker.module';
import {NgbDropdownModule} from '@ng-bootstrap/ng-bootstrap/dropdown/dropdown.module';
import {NgbModalModule} from '@ng-bootstrap/ng-bootstrap/modal/modal.module';
import {NgbNavModule} from '@ng-bootstrap/ng-bootstrap/nav/nav.module';
import {NgbPaginationModule} from '@ng-bootstrap/ng-bootstrap/pagination/pagination.module';
import {NgbPopoverModule} from '@ng-bootstrap/ng-bootstrap/popover/popover.module';
import {NgbProgressbarModule} from '@ng-bootstrap/ng-bootstrap/progressbar/progressbar.module';
import {NgbRatingModule} from '@ng-bootstrap/ng-bootstrap/rating/rating.module';
import {NgbTabsetModule} from '@ng-bootstrap/ng-bootstrap/tabset/tabset.module';
import {NgbTimepickerModule} from '@ng-bootstrap/ng-bootstrap/timepicker/timepicker.module';
import {NgbToastModule} from '@ng-bootstrap/ng-bootstrap/toast/toast.module';
import {NgbTooltipModule} from '@ng-bootstrap/ng-bootstrap/tooltip/tooltip.module';
import {NgbTypeaheadModule} from '@ng-bootstrap/ng-bootstrap/typeahead/typeahead.module';



export {
  NgbAccordion,
  NgbAccordionConfig,
  NgbAccordionModule,
  NgbPanel,
  NgbPanelChangeEvent,
  NgbPanelContent,
  NgbPanelHeader,
  NgbPanelHeaderContext,
  NgbPanelTitle,
  NgbPanelToggle
} from '@ng-bootstrap/ng-bootstrap/accordion/accordion.module';
export {NgbAlert, NgbAlertConfig, NgbAlertModule} from '@ng-bootstrap/ng-bootstrap/alert/alert.module';
export {NgbButtonLabel, NgbButtonsModule, NgbCheckBox, NgbRadio, NgbRadioGroup} from '@ng-bootstrap/ng-bootstrap/buttons/buttons.module';
export {
  NgbCarousel,
  NgbCarouselConfig,
  NgbCarouselModule,
  NgbSlide,
  NgbSlideEvent,
  NgbSlideEventDirection,
  NgbSlideEventSource
} from '@ng-bootstrap/ng-bootstrap/carousel/carousel.module';
export {NgbCollapse, NgbCollapseModule} from '@ng-bootstrap/ng-bootstrap/collapse/collapse.module';
export {
  NgbCalendar,
  NgbCalendarGregorian,
  NgbCalendarHebrew,
  NgbCalendarIslamicCivil,
  NgbCalendarIslamicUmalqura,
  NgbCalendarPersian,
  NgbDate,
  NgbDateAdapter,
  NgbDateNativeAdapter,
  NgbDateNativeUTCAdapter,
  NgbDateParserFormatter,
  NgbDatepicker,
  NgbDatepickerConfig,
  NgbInputDatepickerConfig,
  NgbDatepickerContent,
  NgbDatepickerI18n,
  NgbDatepickerI18nHebrew,
  NgbDatepickerKeyboardService,
  NgbDatepickerModule,
  NgbDatepickerMonth,
  NgbDatepickerNavigateEvent,
  NgbDatepickerState,
  NgbDateStruct,
  NgbInputDatepicker,
  NgbPeriod
} from '@ng-bootstrap/ng-bootstrap/datepicker/datepicker.module';
export {
  NgbDropdown,
  NgbDropdownAnchor,
  NgbDropdownConfig,
  NgbDropdownItem,
  NgbDropdownMenu,
  NgbDropdownModule,
  NgbDropdownToggle,
  NgbNavbar
} from '@ng-bootstrap/ng-bootstrap/dropdown/dropdown.module';
export {
  ModalDismissReasons,
  NgbActiveModal,
  NgbModal,
  NgbModalConfig,
  NgbModalModule,
  NgbModalOptions,
  NgbModalRef
} from '@ng-bootstrap/ng-bootstrap/modal/modal.module';
export {
  NgbNavChangeEvent,
  NgbNavConfig,
  NgbNav,
  NgbNavContent,
  NgbNavContentContext,
  NgbNavItem,
  NgbNavLink,
  NgbNavModule,
  NgbNavOutlet
} from '@ng-bootstrap/ng-bootstrap/nav/nav.module';
export {
  NgbPagination,
  NgbPaginationConfig,
  NgbPaginationEllipsis,
  NgbPaginationFirst,
  NgbPaginationLast,
  NgbPaginationModule,
  NgbPaginationNext,
  NgbPaginationNumber,
  NgbPaginationPrevious
} from '@ng-bootstrap/ng-bootstrap/pagination/pagination.module';
export {NgbPopover, NgbPopoverConfig, NgbPopoverModule} from '@ng-bootstrap/ng-bootstrap/popover/popover.module';
export {NgbProgressbar, NgbProgressbarConfig, NgbProgressbarModule} from '@ng-bootstrap/ng-bootstrap/progressbar/progressbar.module';
export {NgbRating, NgbRatingConfig, NgbRatingModule} from '@ng-bootstrap/ng-bootstrap/rating/rating.module';
export {
  NgbTab,
  NgbTabChangeEvent,
  NgbTabContent,
  NgbTabset,
  NgbTabsetConfig,
  NgbTabsetModule,
  NgbTabTitle
} from '@ng-bootstrap/ng-bootstrap/tabset/tabset.module';
export {
  NgbTimeAdapter,
  NgbTimepickerI18n,
  NgbTimepicker,
  NgbTimepickerConfig,
  NgbTimepickerModule,
  NgbTimeStruct
} from '@ng-bootstrap/ng-bootstrap/timepicker/timepicker.module';
export {NgbToast, NgbToastConfig, NgbToastHeader, NgbToastModule} from '@ng-bootstrap/ng-bootstrap/toast/toast.module';
export {NgbTooltip, NgbTooltipConfig, NgbTooltipModule} from '@ng-bootstrap/ng-bootstrap/tooltip/tooltip.module';
export {
  NgbHighlight,
  NgbTypeahead,
  NgbTypeaheadConfig,
  NgbTypeaheadModule,
  NgbTypeaheadSelectItemEvent
} from '@ng-bootstrap/ng-bootstrap/typeahead/typeahead.module';
export {Placement} from '@ng-bootstrap/ng-bootstrap/util/positioning';


const NGB_MODULES = [
  NgbAccordionModule, NgbAlertModule, NgbButtonsModule, NgbCarouselModule, NgbCollapseModule, NgbDatepickerModule,
  NgbDropdownModule, NgbModalModule, NgbNavModule, NgbPaginationModule, NgbPopoverModule, NgbProgressbarModule,
  NgbRatingModule, NgbTimepickerModule, NgbToastModule, NgbTooltipModule, NgbTypeaheadModule,
  // tslint:disable-next-line:deprecation
  NgbTabsetModule
];

@NgModule({imports: NGB_MODULES, exports: NGB_MODULES})
export class NgbModule {
}
