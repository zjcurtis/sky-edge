from enum import Enum


class GiftValidationErrorInvalidInputErrorCode(str, Enum):
    ACKNOWLEDGEENOTASSOCIATEDWITHTRIBUTE = "AcknowledgeeNotAssociatedWithTribute"
    ADJUSTINGGIFTAFTERPROCESSINGREFUNDFAILED = (
        "AdjustingGiftAfterProcessingRefundFailed"
    )
    AMENDSCHEDULEVALIDATIONNOTAVAILABLE = "AmendScheduleValidationNotAvailable"
    APPLYPAYMENTCANNOTPROVIDEDUPLICATEINSTALLMENTS = (
        "ApplyPaymentCannotProvideDuplicateInstallments"
    )
    AUSTRALIANDIRECTDEBITGIFTCANNOTBEADDED = "AustralianDirectDebitGiftCannotBeAdded"
    AUSTRALIANDIRECTDEBITREQUIRESMANDATEURL = "AustralianDirectDebitRequiresMandateUrl"
    AUTOMATEDPLEDGEINSTALLMENTUPDATEMUSTBEAFTERTODAY = (
        "AutomatedPledgeInstallmentUpdateMustBeAfterToday"
    )
    CANADIANDIRECTDEBITGIFTCANNOTBEADDED = "CanadianDirectDebitGiftCannotBeAdded"
    CANADIANDIRECTDEBITREQUIRESPADMANDATEURL = (
        "CanadianDirectDebitRequiresPADMandateUrl"
    )
    CANNOTADDGIFTTOAPPROVEDBATCH = "CannotAddGiftToApprovedBatch"
    CANNOTCHARGECREDITCARDWITHOUTTRANSACTIONID = (
        "CannotChargeCreditCardWithoutTransactionId"
    )
    CANNOTCHARGEDIRECTDEBITWITHOUTACCOUNTTOKENORTRANSACTIONID = (
        "CannotChargeDirectDebitWithoutAccountTokenOrTransactionId"
    )
    CANNOTCHARGEDIRECTDEBITWITHOUTTRANSACTIONID = (
        "CannotChargeDirectDebitWithoutTransactionId"
    )
    CANNOTUPDATEGIFTINAPPROVEDBATCH = "CannotUpdateGiftInApprovedBatch"
    CFACOMBINATIONINVALID = "CFACombinationInvalid"
    CHARGETRANSACTIONNOTSUPPORTED = "ChargeTransactionNotSupported"
    CHARGETRANSACTIONNOTSUPPORTEDFORGIFTTYPE = (
        "ChargeTransactionNotSupportedForGiftType"
    )
    CONSTITUENTIDNOTFOUND = "ConstituentIdNotFound"
    CREDITCARDTYPEINVALID = "CreditCardTypeInvalid"
    CUSTOMFIELDDESCRIPTIONDOESNOTMATCHCATEGORYDATATYPE = (
        "CustomFieldDescriptionDoesNotMatchCategoryDataType"
    )
    DELETEGIFTOPPORTUNITYTHATDOESNOTEXIST = "DeleteGiftOpportunityThatDoesNotExist"
    DONORCOVERSPLITLESSTHANDONORCOVERAMOUNT = "DonorCoverSplitLessThanDonorCoverAmount"
    DONOTPOSTGIFTMUSTNOTHAVEPOSTDATE = "DoNotPostGiftMustNotHavePostDate"
    DUPLICATEGIFTCHILDITEMS = "DuplicateGiftChildItems"
    DUPLICATEGIFTOPPORTUNITYITEM = "DuplicateGiftOpportunityItem"
    DUPLICATEPERSISTENTKEYSINREQUEST = "DuplicatePersistentKeysInRequest"
    DUPLICATEPLEDGEPARENTIDSPROVIDED = "DuplicatePledgeParentIdsProvided"
    GIFTACCOUNTNUMBERTOOLONG = "GiftAccountNumberTooLong"
    GIFTACKNOWLEDGEMENTLETTERINVALID = "GiftAcknowledgementLetterInvalid"
    GIFTACKNOWLEDGEMENTMUSTHAVEVALIDACKNOWLEDGEMENTSTATUS = (
        "GiftAcknowledgementMustHaveValidAcknowledgementStatus"
    )
    GIFTARGUMENTNOTVALID = "GiftArgumentNotValid"
    GIFTCHARGEFIRSTPAYMENTINVALIDDATE = "GiftChargeFirstPaymentInvalidDate"
    GIFTCHECKNUMBERTOOLONG = "GiftCheckNumberTooLong"
    GIFTCHILDITEMAMOUNTEXCEEDSGIFTAMOUNT = "GiftChildItemAmountExceedsGiftAmount"
    GIFTCHILDITEMINVALIDGUID = "GiftChildItemInvalidGuid"
    GIFTCHILDITEMREQUIREDARGUMENTNOTASSIGNEDVALUE = (
        "GiftChildItemRequiredArgumentNotAssignedValue"
    )
    GIFTCODEINVALID = "GiftCodeInvalid"
    GIFTCONSTITUENCYINVALID = "GiftConstituencyInvalid"
    GIFTCUSTOMFIELDACTIVECATEGORYDOESNOTEXIST = (
        "GiftCustomFieldActiveCategoryDoesNotExist"
    )
    GIFTCUSTOMFIELDCATEGORYISINACTIVE = "GiftCustomFieldCategoryIsInactive"
    GIFTCUSTOMFIELDCOMMENTTOOLONG = "GiftCustomFieldCommentTooLong"
    GIFTCUSTOMFIELDCONSTITUENTDOESNOTEXIST = "GiftCustomFieldConstituentDoesNotExist"
    GIFTCUSTOMFIELDCURRENCYVALUEINVALID = "GiftCustomFieldCurrencyValueInvalid"
    GIFTCUSTOMFIELDFUZZYDATEVALUEINVALID = "GiftCustomFieldFuzzyDateValueInvalid"
    GIFTCUSTOMFIELDINVALIDCATEGORYID = "GiftCustomFieldInvalidCategoryId"
    GIFTCUSTOMFIELDINVALIDCODETABLE = "GiftCustomFieldInvalidCodeTable"
    GIFTCUSTOMFIELDINVALIDNUMERICVALUE = "GiftCustomFieldInvalidNumericValue"
    GIFTCUSTOMFIELDSMULTIPLEONEPERRECORDTYPECATEGORIESADDED = (
        "GiftCustomFieldsMultipleOnePerRecordTypeCategoriesAdded"
    )
    GIFTCUSTOMFIELDTEXTVALUETOOLONG = "GiftCustomFieldTextValueTooLong"
    GIFTDATEFILTERSINVALID = "GiftDateFiltersInvalid"
    GIFTDATEOUTOFRANGEOFGIFTTRIBUTE = "GiftDateOutOfRangeOfGiftTribute"
    GIFTDATEOUTOFVALIDRANGE = "GiftDateOutOfValidRange"
    GIFTDUPLICATEFUNDRAISERS = "GiftDuplicateFundraisers"
    GIFTDUPLICATERECOGNITIONCREDITS = "GiftDuplicateRecognitionCredits"
    GIFTDUPLICATESPLITS = "GiftDuplicateSplits"
    GIFTFUNDRAISERISNOTANACTIVEFUNDRAISER = "GiftFundraiserIsNotAnActiveFundraiser"
    GIFTMUSTBEAPLEDGEPAYMENTTOAPPLYPAYMENT = "GiftMustBeAPledgePaymentToApplyPayment"
    GIFTMUSTBEPLEDGETOSENDREMINDER = "GiftMustBePledgeToSendReminder"
    GIFTNEGATIVEAMOUNTARGUMENTFOUND = "GiftNegativeAmountArgumentFound"
    GIFTNONCHECKNONDIRECTDEBITPAYMENTMUSTNOTHAVECHECKNUMBER = (
        "GiftNonCheckNonDirectDebitPaymentMustNotHaveCheckNumber"
    )
    GIFTNONCHECKPAYMENTMUSTNOTHAVECHECKDATE = "GiftNonCheckPaymentMustNotHaveCheckDate"
    GIFTNONCHECKPAYMENTMUSTNOTHAVEDRAWER = "GiftNonCheckPaymentMustNotHaveDrawer"
    GIFTNONCREDITCARDPAYMENTMUSTNOTHAVEAUTHORIZATIONCODE = (
        "GiftNonCreditCardPaymentMustNotHaveAuthorizationCode"
    )
    GIFTNONCREDITCARDPAYMENTMUSTNOTHAVECARDHOLDER = (
        "GiftNonCreditCardPaymentMustNotHaveCardholder"
    )
    GIFTNONCREDITCARDPAYMENTMUSTNOTHAVECARDTYPE = (
        "GiftNonCreditCardPaymentMustNotHaveCardType"
    )
    GIFTONLYONEITEMALLOWED = "GiftOnlyOneItemAllowed"
    GIFTOPPORTUNITYAMOUNTCANNOTEXCEEDGIFTAMOUNT = (
        "GiftOpportunityAmountCannotExceedGiftAmount"
    )
    GIFTOPPORTUNITYARGUMENTEMPTY = "GiftOpportunityArgumentEmpty"
    GIFTOPPORTUNITYARGUMENTNOTVALID = "GiftOpportunityArgumentNotValid"
    GIFTORIGININVALIDJSON = "GiftOriginInvalidJSON"
    GIFTORIGINMISSINGNAME = "GiftOriginMissingName"
    GIFTORIGINTOOLONG = "GiftOriginTooLong"
    GIFTPACKAGEREQUESTEDAPPEALNOTSPECIFIED = "GiftPackageRequestedAppealNotSpecified"
    GIFTPAYMENTINFORMATIONNOTAVAILABLEFORAMENDMENT = (
        "GiftPaymentInformationNotAvailableForAmendment"
    )
    GIFTPAYMENTMETHODINVALID = "GiftPaymentMethodInvalid"
    GIFTPAYMENTMETHODMUSTBECREDITCARDTOPROCESSREFUND = (
        "GiftPaymentMethodMustBeCreditCardToProcessRefund"
    )
    GIFTPAYMENTMISSINGAMOUNT = "GiftPaymentMissingAmount"
    GIFTPAYMENTMUSTBEGREATERTHANZEROTOPROCESSREFUND = (
        "GiftPaymentMustBeGreaterThanZeroToProcessRefund"
    )
    GIFTPAYMENTMUSTHAVETRANSACTIONIDTOPROCESSREFUND = (
        "GiftPaymentMustHaveTransactionIdToProcessRefund"
    )
    GIFTPAYMENTTRANSACTIONIDMUSTBEVALIDGUIDTOPROCESSREFUND = (
        "GiftPaymentTransactionIdMustBeValidGuidToProcessRefund"
    )
    GIFTRECEIPTHASSTACKFIELDSBUTCAPABILITYNOTENABLED = (
        "GiftReceiptHasStackFieldsButCapabilityNotEnabled"
    )
    GIFTRECEIPTMUSTHAVEVALIDRECEIPTSTATUS = "GiftReceiptMustHaveValidReceiptStatus"
    GIFTRECEIPTSTACKDOESNOTEXIST = "GiftReceiptStackDoesNotExist"
    GIFTRECEIPTSTACKNOTUNIQUE = "GiftReceiptStackNotUnique"
    GIFTREFERENCENUMBERTOOLONG = "GiftReferenceNumberTooLong"
    GIFTSPLITMISSINGFUNDID = "GiftSplitMissingFundId"
    GIFTSPLITTOTALAMOUNTDOESNOTEQUALGIFTAMOUNT = (
        "GiftSplitTotalAmountDoesNotEqualGiftAmount"
    )
    GIFTSUBTYPEINVALID = "GiftSubtypeInvalid"
    GIFTTRIBUTEACKNOWLEDGEEDOESNOTEXIST = "GiftTributeAcknowledgeeDoesNotExist"
    GIFTTRIBUTEACKNOWLEDGEELETTERINVALID = "GiftTributeAcknowledgeeLetterInvalid"
    GIFTTRIBUTEALREADYEXISTS = "GiftTributeAlreadyExists"
    GIFTTRIBUTEDOESNOTEXIST = "GiftTributeDoesNotExist"
    GIFTTRIBUTEISINACTIVE = "GiftTributeIsInactive"
    GIFTTYPECANNOTBEAMENDED = "GiftTypeCannotBeAmended"
    GIFTTYPENOTPERMITTED = "GiftTypeNotPermitted"
    GIFTUNSUPPORTEDPAYMENTMETHOD = "GiftUnsupportedPaymentMethod"
    GIFTWITHACKNOWLEDGEMENTLETTERHASANINVALIDACKNOWLEDGEMENTSTATUS = (
        "GiftWithAcknowledgementLetterHasAnInvalidAcknowledgementStatus"
    )
    GIFTWITHDONORCOVERCANNOTBEAPPLIEDTOPLEDGE = (
        "GiftWithDonorCoverCannotBeAppliedToPledge"
    )
    INSTALLMENTPAYMENTAMOUNTMUSTMATCHINSTALLMENTBALANCE = (
        "InstallmentPaymentAmountMustMatchInstallmentBalance"
    )
    INSTALLMENTSMUSTEXISTTOAPPLYPAYMENT = "InstallmentsMustExistToApplyPayment"
    INVALIDAPPLYPAYMENTSFORBATCHRECURRINGPAYMENT = (
        "InvalidApplyPaymentsForBatchRecurringPayment"
    )
    INVALIDBATCHID = "InvalidBatchId"
    INVALIDEXTENSIONID = "InvalidExtensionId"
    INVALIDGIFTID = "InvalidGiftId"
    INVALIDGIFTSTATUS = "InvalidGiftStatus"
    INVALIDGIFTSTATUSAMENDGIFT = "InvalidGiftStatusAmendGift"
    INVALIDGIFTTYPE = "InvalidGiftType"
    INVALIDID = "InvalidId"
    INVALIDNUMBEROFINSTALLMENTSFORSINGLESCHEDULE = (
        "InvalidNumberOfInstallmentsForSingleSchedule"
    )
    INVALIDOPPORTUNITYID = "InvalidOpportunityId"
    INVALIDPAYMENTCONFIGURATIONID = "InvalidPaymentConfigurationId"
    INVALIDSCHEDULEDINSTALLMENTDATEAMENDGIFT = (
        "InvalidScheduledInstallmentDateAmendGift"
    )
    INVALIDTRIBUTEID = "InvalidTributeId"
    LINKEDRECURRINGGIFTDOESNOTEXIST = "LinkedRecurringGiftDoesNotExist"
    LOOKUPIDNOTUNIQUE = "LookupIdNotUnique"
    MISSINGIFMATCHHEADER = "MissingIfMatchHeader"
    NONACKNOWLEDGEDGIFTCANNOTHAVEACKNOWLEDGEMENTDATE = (
        "NonAcknowledgedGiftCannotHaveAcknowledgementDate"
    )
    NONRECEIPTEDGIFTCANNOTHAVERECEIPTDATE = "NonReceiptedGiftCannotHaveReceiptDate"
    NONRECURRINGGIFTCANNOTHAVESCHEDULE = "NonRecurringGiftCannotHaveSchedule"
    NONSTOCKGIFTCANNOTHAVEISSUERDETAILS = "NonStockGiftCannotHaveIssuerDetails"
    NUMBEROFINSTALLMENTSEXCEEDSMAXAMOUNT = "NumberOfInstallmentsExceedsMaxAmount"
    NUMBEROFINSTALLMENTSMUSTBEPOSITIVE = "NumberOfInstallmentsMustBePositive"
    NUMBEROFTRANSACTIONIDSPROVIDEDEXCEEDSLIMIT = (
        "NumberOfTransactionIdsProvidedExceedsLimit"
    )
    PADMANDATESAREINVALIDFORGIFT = "PADMandatesAreInvalidForGift"
    PAYMENTAMENDMENTIDANDORIGINALGIFTIDMISMATCH = (
        "PaymentAmendmentIdAndOriginalGiftIdMismatch"
    )
    PAYMENTAMENDMENTMISSINGORIGINALGIFT = "PaymentAmendmentMissingOriginalGift"
    PERSISTENTKEYALREADYEXISTS = "PersistentKeyAlreadyExists"
    PLEDGEINSTALLMENTARGUMENTNOTVALID = "PledgeInstallmentArgumentNotValid"
    PLEDGEINSTALLMENTDATEMUSTBESET = "PledgeInstallmentDateMustBeSet"
    PLEDGEINSTALLMENTDATEMUSTNOTPRECEDEGIFTDATE = (
        "PledgeInstallmentDateMustNotPrecedeGiftDate"
    )
    PLEDGEINSTALLMENTGENERATIONNUMBEROFINSTALLMENTSANDENDDATESET = (
        "PledgeInstallmentGenerationNumberOfInstallmentsAndEndDateSet"
    )
    PLEDGEINSTALLMENTNEGATIVEAMOUNTARGUMENTFOUND = (
        "PledgeInstallmentNegativeAmountArgumentFound"
    )
    PLEDGEINSTALLMENTPARENTGIFTISNOTPLEDGE = "PledgeInstallmentParentGiftIsNotPledge"
    PLEDGEINSTALLMENTSTOTALDOESNOTMATCHGIFTAMOUNT = (
        "PledgeInstallmentsTotalDoesNotMatchGiftAmount"
    )
    PLEDGEPAYMENTINSTALLMENTCANNOTBEAPPLIEDTOPASTORCURRENTAUTOMATEDINSTALLMENTS = (
        "PledgePaymentInstallmentCannotBeAppliedToPastOrCurrentAutomatedInstallments"
    )
    PLEDGEPAYMENTPARENTGIFTISNOTPLEDGE = "PledgePaymentParentGiftIsNotPledge"
    PLEDGESCHEDULEAMOUNTMUSTBEATLEASTONETOBEDISTRIBUTEDTOMORETHANONEINSTALLMENT = (
        "PledgeScheduleAmountMustBeAtLeastOneToBeDistributedToMoreThanOneInstallment"
    )
    PLEDGESCHEDULEINVALID = "PledgeScheduleInvalid"
    PLEDGEWITHIRREGULARSCHEDULEMUSTHAVEINSTALLMENTS = (
        "PledgeWithIrregularScheduleMustHaveInstallments"
    )
    PLEDGEWITHSINGLEFREQUENCYMUSTHAVEEXACTLYONEINSTALLMENT = (
        "PledgeWithSingleFrequencyMustHaveExactlyOneInstallment"
    )
    POSTEDGIFTCANNOTBEMODIFIED = "PostedGiftCannotBeModified"
    PROCESSREFUNDREQUESTNOTVALID = "ProcessRefundRequestNotValid"
    RECEIPTEDGIFTMUSTHAVERECEIPTDATE = "ReceiptedGiftMustHaveReceiptDate"
    RECURRINGGIFTCANNOTBERECEIPTED = "RecurringGiftCannotBeReceipted"
    RECURRINGGIFTCANNOTBEREFUNDED = "RecurringGiftCannotBeRefunded"
    REQUESTEDGIFTLOOKUPIDOUTOFRANGE = "RequestedGiftLookupIdOutOfRange"
    REQUIREDARGUMENTNOTASSIGNEDVALUE = "RequiredArgumentNotAssignedValue"
    SCHEDULEINVALIDENDDATE = "ScheduleInvalidEndDate"
    SCHEDULEINVALIDFREQUENCY = "ScheduleInvalidFrequency"
    SCHEDULEINVALIDSTARTDATE = "ScheduleInvalidStartDate"
    SCHEDULESTARTDATEMISSING = "ScheduleStartDateMissing"
    SOLDSTOCKDETAILSARGUMENTNOTVALID = "SoldStockDetailsArgumentNotValid"
    STOCKISSUERDETAILSARGUMENTNOTVALID = "StockIssuerDetailsArgumentNotValid"
    SUMOFAMOUNTAPPLIEDDOESNOTEQUALGIFTAMOUNT = (
        "SumOfAmountAppliedDoesNotEqualGiftAmount"
    )
    TRANSACTIONCAPTUREFAILEDWITHPROVIDEDTRANSACTIONID = (
        "TransactionCaptureFailedWithProvidedTransactionId"
    )
    TRANSACTIONDATEMUSTBEWITHINONEYEARTOPROCESSREFUND = (
        "TransactionDateMustBeWithinOneYearToProcessRefund"
    )
    TRANSACTIONDETAILSUPDATEFAILED = "TransactionDetailsUpdateFailed"
    TRANSACTIONGATEWAYIDMUSTBEBBMSTOPROCESSREFUND = (
        "TransactionGatewayIdMustBeBBMSToProcessRefund"
    )
    TRANSACTIONIDCOULDNOTBEFOUND = "TransactionIdCouldNotBeFound"
    TRANSACTIONRESULTCODEMUSTBEAPPROVEDTOPROCESSREFUND = (
        "TransactionResultCodeMustBeApprovedToProcessRefund"
    )
    UKDIRECTDEBITGIFTCANNOTBEADDED = "UKDirectDebitGiftCannotBeAdded"
    UKDIRECTDEBITREQUIRESMANDATEURL = "UKDirectDebitRequiresMandateUrl"
    UNAUTHORIZEDEXCEPTION = "UnauthorizedException"
    UNPOSTABLEGIFTTYPEMARKEDPOSTABLE = "UnpostableGiftTypeMarkedPostable"
    UNPROVISIONEDBBPSACCOUNT = "UnprovisionedBbpsAccount"
    UPDATEDGIFTAMOUNTLESSTHANAMOUNTSUBJECTTOVAT = (
        "UpdatedGiftAmountLessThanAmountSubjectToVat"
    )
    UPDATEDGIFTAMOUNTLESSTHANOPPORTUNITYAPPLIEDAMOUNT = (
        "UpdatedGiftAmountLessThanOpportunityAppliedAmount"
    )
    UPDATEDGIFTAMOUNTLESSTHANTOTALBENEFITSAMOUNT = (
        "UpdatedGiftAmountLessThanTotalBenefitsAmount"
    )
    UPDATEDRECURRINGGIFTAMOUNTTOZERO = "UpdatedRecurringGiftAmountToZero"
    UPDATEGIFTOPPORTUNITYTHATDOESNOTEXIST = "UpdateGiftOpportunityThatDoesNotExist"
    UPDATEGIFTSTATUSINVALIDGIFTSTATUS = "UpdateGiftStatusInvalidGiftStatus"
    UPDATEPLEDGEINSTALLMENTTHATDOESNOTEXIST = "UpdatePledgeInstallmentThatDoesNotExist"

    def __str__(self) -> str:
        return str(self.value)
