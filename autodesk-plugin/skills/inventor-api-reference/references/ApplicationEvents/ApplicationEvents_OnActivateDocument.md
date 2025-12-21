# ApplicationEvents.OnActivateDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that is fired whenever a document is activated.

## Remarks

The OnActivateDocument event notifies a client when a document is activated. The definition of an active document is the top-level document that is being displayed in the active window. The title of a window also indicates the active document for that window. It's also important to understand that the document currently being edited is not necessarily the active document. This happens in the case of in-place editing in the context of an assembly. When you open an assembly document, the assembly is the active document. If you in-place edit a part within the assembly, the assembly is still the active document. The part being edited is the active edit object. The ApplicationEvents.OnNewEditObject event provides notification when the active edit object changes and the Application.ActiveEditObject property returns the current active edit object.

## Syntax

ApplicationEvents.**OnActivateDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input object that is being activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the document is activated. Notification is sent before and after the document is activated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 4
