# ApplicationEvents.OnNewEditObject Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnNewEditObject event notifies a client when the edit object is changing.

## Remarks

This event is useful in many cases but is particularly critical when adding additional tabs to the browser. This event serves as the notification of when to add the browser tab. The OnOpenDocument event is not satisfactory for this case because this event is fired for documents that are opened as a result of being referenced in an assembly. In this context, most of the documents will not be directly edited, so adding the browser information is a waste of resources. The OnActivateDocument event is also unsatisfactory because when a document is edited in the context of an assembly, it is not activated. The assembly remains the active document. What does change is the current edit object. The edit object is the container object that is being edited by the end-user. For example when an assembly document is opened, the assembly document is the active document and the active edit object. If the end-user in-place activates a part in the assembly, the part becomes the active edit object, although the assembly is still the active document because the edit is taking place in the context of the assembly. If the end-user creates or edits a sketch within the part, the sketch becomes the active edit object. Valid objects for edit objects are documents, 2d and 3d sketches, and drawing sheets.

## Syntax

ApplicationEvents.**OnNewEditObject**( ***EditObject*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EditObject | Object | The new edit object. When the BeforeOrAfter argument is kBefore this is the object that will become the edit object. When the argument is kAfter this is the current edit object. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) there is a new edit object. Notification is sent before and after the edit object change is made. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. When an object is activated for edit within the context of an assembly some additional information is provided through the Context argument, as described below: Name = "ActiveDocument", Value = The AssemblyDocument object that the edit is within the context of. Name = "ActiveEditObject", Value = The ComponentOccurrence object in the assembly the edit is through. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Notes

A scenario that users need to be aware of is when you use this event to monitor opening a drawing document, the active edit object(i.e. active sheet in the drawing in this case) will be available but its parent drawing document still not becomes the active document, in this case users need to get the parent drawing document from the Sheet.Parent.

## Version

Introduced in version 5
