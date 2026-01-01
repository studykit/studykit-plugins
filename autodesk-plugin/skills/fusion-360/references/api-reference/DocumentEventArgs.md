# DocumentEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

The DocumentEventArgs provides information associated with a document event. Note that some properties are not available on every event - for example, the Document is not available on the DocumentOpening event because the Document is not yet available.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DocumentEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [cancelReason](DocumentEventArgs_cancelReason.htm) | Gets and sets the description of the reason why the operation is being canceled. This property is only used if isOperationCancelled is set to true. |
| [document](DocumentEventArgs_document.htm) | Provides access to the document that is open. Can be null in the case where the event is fired before the document has been opened or after it has been closed. |
| [firingEvent](DocumentEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [fullPath](DocumentEventArgs_fullPath.htm) | The full path to the file. |
| [isOperationCancelled](DocumentEventArgs_isOperationCancelled.htm) | Gets and sets if the operation for this event is to be canceled. The description of the reason for canceling the operation can be set with the cancelReason property. This is only supported for the documentSaving event. |
| [isValid](DocumentEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DocumentEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |