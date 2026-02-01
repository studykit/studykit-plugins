# DataEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

A Data event is an event associated with operations on Data items.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DataEvent_add.htm) | Add a handler to be notified when the data event occurs. |
| [classType](DataEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](DataEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](DataEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](DataEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](DataEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](DataEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Application.dataFileComplete](Application_dataFileComplete.htm), [Application.dataFileCopyComplete](Application_dataFileCopyComplete.htm)

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |