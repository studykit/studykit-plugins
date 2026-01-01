# PresentationEvents.OnPublicationNameChange Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication component’s name is changed.

## Syntax

PresentationEvents.**OnPublicationNameChange**( ***DocumentObject*** As [PresentationDocument](../PresentationDocument/PresentationDocument.md), ***PublicationObj*** As [Publication](Publication.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [PresentationDocument](../PresentationDocument/PresentationDocument.md) | The PresentationDocument where the name has changed. |
| PublicationObj | [Publication](Publication.md) | The Publication object whose name has changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the Presentation’s name is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument is currently ignored for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
