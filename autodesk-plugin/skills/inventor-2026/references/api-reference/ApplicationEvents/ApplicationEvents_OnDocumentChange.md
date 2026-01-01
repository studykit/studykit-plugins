# ApplicationEvents.OnDocumentChange Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Fires just before the document is changed, supplying the reasons for change and the context in which this action is being taken.

## Remarks

The OnDocumentChange event notifies a client when an action occurs that causes any change to a document. The context information can be used to determine what the change is. The notification is not sent for commands that do not change the document, i.e. measure and view commands. Care needs to be taken when using this event because changes to the document are made so frequently that depending on what you do in response to the event it can degrade the performance of Inventor. You should perform simple checks first to see if the change is one that you're interested in before you perform more expensive operations. Whenever possible you should use more specific events instead of this general change event. For example, if you're interested in knowing when a parameter value changes you can listen to the ModelingEvents.OnParameterChange event instead. This is both simpler for you and more efficient, but not all actions that can occur within Inventor have corresponding events so in many cases using the OnDocumentChange event is the only solution. When an object is deleted from the document, it is possible to find out what that object is by querying Document.SelectSet while in the kBefore state of this event.

## Syntax

ApplicationEvents.**OnDocumentChange**( ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***ReasonsForChange*** As [CommandTypesEnum](../CommandTypesEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the change is occurring within. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. This argument specifies if the notification is being sent before a change is made (kBefore), after a change is made (kAfter), or when a change has been aborted (kAbort). |
| ReasonsForChange | [CommandTypesEnum](../CommandTypesEnum.md) | This argument indicates the type of change that occurred. The value is from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument provides additional information as described below:  Name = "DisplayName", Value = The display name of the command that caused the change. This name will change based on the language currently being used for Inventor.  Name = "InternalName", Value = The internal name of the command that caused the change. This name will be consistent regardless of the current language.  Name = "InternalNamesList", Value = as follows. When the internal name is "CompositeChange" this value is returned. Some commands result in making several changes but combine or composite them into a single command. The individual changes that were composited into the single command are provided through this value. It is an array of strings that consist of the internal names of the individual changes made. For example, if you drag a sketch point that connects two lines, the display name is "Drag Sketch Inference", the internal name is "CompositeChange" and the internal names list is an array of the following three strings; "Modify Point", "Modify Line", and "Modify Line".  Name = "ConsideredDirty", Value = "". If this name appears in the context list then the change made is one that causes the document to be dirty. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This event supports the ability to cancel the change. By setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore Inventor will abort the change. When the change is cancelled, this event is fired again but the BeforeOrAfter argument will have a value of kAbort. |

## Version

Introduced in version 8
