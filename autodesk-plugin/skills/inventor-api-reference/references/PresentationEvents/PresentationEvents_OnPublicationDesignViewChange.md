# PresentationEvents.OnPublicationDesignViewChange Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication design view is changed.

## Syntax

PresentationEvents.**OnPublicationDesignViewChange**( ***DocumentObject*** As [PresentationDocument](../PresentationDocument/PresentationDocument.md), ***PublicationObj*** As [Publication](Publication.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [PresentationDocument](../PresentationDocument/PresentationDocument.md) | The PresentationDocument where the change has taken place. |
| PublicationObj | [Publication](Publication.md) | The Publication object where the design view has changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the Presentation’s design view is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument is currently ignored for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
