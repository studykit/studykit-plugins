# SetupChangeEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEvent.h>

## Description

A SetupChangeEvent represents a setup related change event. It is used for SetupChanged notifications.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SetupChangeEvent_add.htm) | Add a handler to be notified when the file event occurs. |
| [classType](SetupChangeEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](SetupChangeEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](SetupChangeEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](SetupChangeEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](SetupChangeEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](SetupChangeEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[CAM.setupChanged](CAM_setupChanged.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |