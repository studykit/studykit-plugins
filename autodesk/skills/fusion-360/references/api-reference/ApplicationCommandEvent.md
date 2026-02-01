# ApplicationCommandEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

An event endpoint that supports the connection to ApplicationCommandEventHandlers.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ApplicationCommandEvent_add.htm) | Adds an event handler object to this event endpoint. |
| [classType](ApplicationCommandEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](ApplicationCommandEvent_remove.htm) | Removes a handler from this event endpoint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ApplicationCommandEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ApplicationCommandEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](ApplicationCommandEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](ApplicationCommandEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[UserInterface.commandCreated](UserInterface_commandCreated.htm), [UserInterface.commandStarting](UserInterface_commandStarting.htm), [UserInterface.commandTerminated](UserInterface_commandTerminated.htm)

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |