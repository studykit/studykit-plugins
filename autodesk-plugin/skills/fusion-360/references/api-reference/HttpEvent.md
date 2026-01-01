# HttpEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

A HttpEvent represents an event that occurs in reaction to a http request.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](HttpEvent_add.htm) | Add a handler to be notified when the event occurs. |
| [classType](HttpEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](HttpEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](HttpEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](HttpEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](HttpEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](HttpEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[HttpRequest.completed](HttpRequest_completed.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |