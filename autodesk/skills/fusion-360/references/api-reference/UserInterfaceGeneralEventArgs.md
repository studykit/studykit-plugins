# UserInterfaceGeneralEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEventArgs.h>

## Description

The UserInterfaceGeneralEventArgs is passed when a UserInterfaceGeneralEvent is fired.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](UserInterfaceGeneralEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](UserInterfaceGeneralEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](UserInterfaceGeneralEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](UserInterfaceGeneralEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |