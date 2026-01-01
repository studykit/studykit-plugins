# DocumentEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEvent.h>

## Description

A DocumentEvent represents a document related event. For example, DocumentOpening or DocumentOpened.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DocumentEvent_add.htm) | Add a handler to be notified when the file event occurs. |
| [classType](DocumentEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](DocumentEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](DocumentEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](DocumentEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](DocumentEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](DocumentEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Application.documentActivated](Application_documentActivated.htm), [Application.documentActivating](Application_documentActivating.htm), [Application.documentClosed](Application_documentClosed.htm), [Application.documentClosing](Application_documentClosing.htm), [Application.documentCreated](Application_documentCreated.htm), [Application.documentDeactivated](Application_documentDeactivated.htm), [Application.documentDeactivating](Application_documentDeactivating.htm), [Application.documentOpened](Application_documentOpened.htm), [Application.documentOpening](Application_documentOpening.htm), [Application.documentSaved](Application_documentSaved.htm), [Application.documentSaving](Application_documentSaving.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |