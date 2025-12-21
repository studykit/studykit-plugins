# PresentationEvents.OnNewPublicationMarkedView Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication marked view is added.

## Syntax

PresentationEvents.**OnNewPublicationMarkedView**( ***DocumentObject*** As [PresentationDocument](../PresentationDocument/PresentationDocument.md), ***PublicationObj*** As [Publication](Publication.md), ***PublicationMarkedViewObj*** As [PublicationMarkedView](PublicationMarkedView.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [PresentationDocument](../PresentationDocument/PresentationDocument.md) | The Presentation document the marked view was created in. |
| PublicationObj | [Publication](Publication.md) | The Publication object the marked view was created in. |
| PublicationMarkedViewObj | [PublicationMarkedView](PublicationMarkedView.md) | Input the newly added PublicationMarkedView object. This returns Nothing in the kBefore case. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the PresentationSnapshotView is added. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This event provides additional information through the Context argument as described below: Name = “CreatedForDrawingViewCreation”. Value = Boolean that indicates whether this PresentationSnapshotView is created in drawing view creation dialog for place a new drawing view. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
