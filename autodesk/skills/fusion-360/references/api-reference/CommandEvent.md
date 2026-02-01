# CommandEvent Object

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEvent.h>

## Description

An event endpoint that supports the connection to client implemented CommandEventHandlers.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CommandEvent_add.htm) | Adds an event handler object to this event endpoint. |
| [classType](CommandEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](CommandEvent_remove.htm) | Removes a handler from this event endpoint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CommandEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](CommandEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](CommandEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](CommandEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[Command.activate](Command_activate.htm), [Command.deactivate](Command_deactivate.htm), [Command.destroy](Command_destroy.htm), [Command.execute](Command_execute.htm), [Command.executePreview](Command_executePreview.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |