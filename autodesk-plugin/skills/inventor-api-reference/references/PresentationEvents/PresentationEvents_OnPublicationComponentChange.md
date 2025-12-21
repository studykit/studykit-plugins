# PresentationEvents.OnPublicationComponentChange Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication component is changed.

## Syntax

PresentationEvents.**OnPublicationComponentChange**( ***DocumentObject*** As [PresentationDocument](../PresentationDocument/PresentationDocument.md), ***PublicationComponent*** As [PublicationComponent](PublicationComponent.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [PresentationDocument](../PresentationDocument/PresentationDocument.md) | The PresentationDocument that whose PublicationComponent has changed. |
| PublicationComponent | [PublicationComponent](PublicationComponent.md) | The PublicComponent that changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the PresentationComponent is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Information describing the change is passed through the context argument, as described below:  Name = "Appearance", Value = Asset. Indicates the appearance is changing. The value indicates the new Appearance asset of the PresentationComponent. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) |  |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |