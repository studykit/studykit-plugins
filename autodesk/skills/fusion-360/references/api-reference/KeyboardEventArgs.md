# KeyboardEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

Provides a set of arguments from a firing KeyboardEvent to a KeyboardEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](KeyboardEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](KeyboardEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](KeyboardEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [keyCode](KeyboardEventArgs_keyCode.htm) | Gets the keyboard key. |
| [modifierMask](KeyboardEventArgs_modifierMask.htm) | Gets the set of keyboard modifiers that were active. The value is the Boolean combination of KeyboardModifiers values. |
| [objectType](KeyboardEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |