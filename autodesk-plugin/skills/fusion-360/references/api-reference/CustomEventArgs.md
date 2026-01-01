# CustomEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventArgs.h>

## Description

The ApplicationEventArgs provides information associated with an application event. Note that some properties are not available on every event

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [additionalInfo](CustomEventArgs_additionalInfo.htm) | Information being passed to the add-in in the primary thread from the worker thread or other add-in. |
| [firingEvent](CustomEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](CustomEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Event for Command Dialog](CustomEventCommandDialog_Sample.htm) | Demonstrates using a custom event to process getting information in the background to display in a command dialog. This is an add-in and should be copied and pasted into an add-in project. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |