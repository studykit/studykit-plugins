# MouseEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEvent.h>

## Description

An event endpoint that supports the connection to client implemented MouseEventHandlers.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MouseEvent_add.htm) | Adds an event handler to this event endpoint. |
| [classType](MouseEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](MouseEvent_remove.htm) | Removes a handler from this event endpoint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MouseEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](MouseEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](MouseEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](MouseEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Command.mouseClick](Command_mouseClick.htm), [Command.mouseDoubleClick](Command_mouseDoubleClick.htm), [Command.mouseDown](Command_mouseDown.htm), [Command.mouseDrag](Command_mouseDrag.htm), [Command.mouseDragBegin](Command_mouseDragBegin.htm), [Command.mouseDragEnd](Command_mouseDragEnd.htm), [Command.mouseMove](Command_mouseMove.htm), [Command.mouseUp](Command_mouseUp.htm), [Command.mouseWheel](Command_mouseWheel.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |