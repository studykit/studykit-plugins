# ApplicationCommandEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

Provides a set of arguments from a firing ApplicationCommandEvent to an ApplicationCommandEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ApplicationCommandEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [commandDefinition](ApplicationCommandEventArgs_commandDefinition.htm) | Returns the CommandDefinition object for the command the event is being fired for. |
| [commandId](ApplicationCommandEventArgs_commandId.htm) | Returns the unique id of the command the event if being fired for. |
| [firingEvent](ApplicationCommandEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isCanceled](ApplicationCommandEventArgs_isCanceled.htm) | Used during the commandStarting event to get or set if the command should be allowed to continue executing or be canceled. This defaults to false, which will allow the command to execute. Setting this to true will cancel the command and not begin the execution. This property should be ignored for all events besides the commandStarting event. |
| [isValid](ApplicationCommandEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ApplicationCommandEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [terminationReason](ApplicationCommandEventArgs_terminationReason.htm) | Returns the reason the command is being terminated. This property should be ignored for all events besides the commandTerminated event. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |