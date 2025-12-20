# RepresentationEvents.OnNewSectionView Event

Parent Object: [RepresentationEvents](../RepresentationEvents/RepresentationEvents.md)

## Description

Event that is fired whenever an section view is created in part or assembly.

## Syntax

RepresentationEvents.**OnNewSectionView**( ***DocumentObject*** As [Document](../Document/Document.md), ***Representation*** As [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Representation | [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md) | Input DesignViewRepresentation object that the section view is created in. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the section view is created. This notification is currently only provided after the section view is created so this is always kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. Name = “SectionViewType”. Value = A value from SectionViewTypeEnum that indicates which type of section view is just created or section view is ended. Name = “FirstSectionPlane”. Value = A Plane object that indicates the first section plane for quarter or three quarter section view and the section plane for the half section view. The normal of the section plane defines the section direction. Name = “SecondSectionPlane”. Value = A Plane object that indicates the second section plane for quarter or three quarter section view. The normal of the section plane defines the section direction. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |