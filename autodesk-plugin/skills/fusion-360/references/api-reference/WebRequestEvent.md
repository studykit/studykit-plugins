# WebRequestEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEvent.h>

## Description

A WebRequestEvent represents an event that occurs in reaction to a Fusion protocol handler in a web page. For example, insertedFromURL and openedFromURL

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](WebRequestEvent_add.htm) | Add a handler to be notified when the event occurs. |
| [classType](WebRequestEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](WebRequestEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](WebRequestEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](WebRequestEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](WebRequestEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](WebRequestEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Application.insertedFromURL](Application_insertedFromURL.htm), [Application.insertingFromURL](Application_insertingFromURL.htm), [Application.openedFromURL](Application_openedFromURL.htm), [Application.openingFromURL](Application_openingFromURL.htm)

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |