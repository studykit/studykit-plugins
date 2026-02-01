# DocumentEvents.OnChange Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

Fires when this document changes, supplying the reasons for change and the context in which this action is being taken.

## Remarks

The notification is not sent for commands that do not change the document, i.e. measure and view commands. Care needs to be taken when using this event because changes to the document are made so frequently that depending on what you do in response to the event it can degrade the performance of Inventor. You should perform simple checks first to see if the change is one that you're interested in before you perform more expensive operations. Whenever possible you should use more specific events instead of this general change event. For example, if you're interested in knowing when a parameter value changes you can listen to the ModelingEvents.OnParameterChange event instead. This is both simpler for you and more efficient, but not all actions that can occur within Inventor have corresponding events so in many cases using the OnChange event is the only solution. There is also a corresponding OnDocumentChange event on the ApplicationEvents object. The OnDocumentChange event notifies clients for changes in all documents. Whereas the OnChange event only sends notification for changes made to the document the event object was obtained from.

## Syntax

DocumentEvents.**OnChange**( ***ReasonsForChange*** As [CommandTypesEnum](../CommandTypesEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReasonsForChange | [CommandTypesEnum](../CommandTypesEnum.md) | This argument indicates the type of change that occurred. The value is from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | This argument specifies if the notification is being sent before a change is made (kBefore), after a change is made (kAfter), or when a change has been aborted (kAbort). |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument provides additional information as described below:  Name = "DisplayName", Value = The display name of the command that caused the change. This name will change based on the language currently being used for Inventor.  Name = "InternalName", Value = The internal name of the command that caused the change. This name will be consistent regardless of the current language.  Name = "InternalNamesList", Value = as follows. When the internal name is "CompositeChange" this value is returned. Some commands result in making several changes but combine or composite them into a single command. The individual changes that were composited into the single command are provided through this value. It is an array of strings that consist of the internal names of the individual changes made. For example, if you drag a sketch point that connects two lines, the display name is "Drag Sketch Inference", the internal name is "CompositeChange" and the internal names list is an array of the following three strings; "Modify Point", "Modify Line", and "Modify Line".  Name = "ConsideredDirty", Value = "". If this name appears in the context list then the change made is one that causes the document to be dirty. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. This event supports the ability to cancel the change. By setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore Inventor will abort the change. When the change is cancelled, this event is fired again but the BeforeOrAfter argument will have a value of kAbort. |

## Version

Introduced in version 8
