# SetupChangeEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventArgs.h>

## Description

The SetupChangeEventArgs provides information associated with a change event of a setup.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SetupChangeEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](SetupChangeEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [info](SetupChangeEventArgs_info.htm) | Provides access to an information string. The optional string may contain additional information about the change. |
| [isValid](SetupChangeEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SetupChangeEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [setup](SetupChangeEventArgs_setup.htm) | Provides access to the setup. Can be null in the case where the event is fired before the setup has been created or after it has been deleted. |
| [type](SetupChangeEventArgs_type.htm) | The type specifies the actual change. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |