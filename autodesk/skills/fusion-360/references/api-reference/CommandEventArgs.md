# CommandEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

Provides a set of arguments from a firing CommandEvent to a CommandEventHandler's notify callback method.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CommandEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [command](CommandEventArgs_command.htm) | Gets the Command object. |
| [executeFailed](CommandEventArgs_executeFailed.htm) | Used during the execute event to get or set that the execute operations failed and the commands transaction should be aborted. This property should be ignored for all events besides the Execute event. |
| [executeFailedMessage](CommandEventArgs_executeFailedMessage.htm) | Used during the execute event to get or set a description of an execute failure. This property should be ignored for all events besides the Execute event. |
| [firingEvent](CommandEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](CommandEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isValidResult](CommandEventArgs_isValidResult.htm) | Used during the commandStarting event to get or set that the result of preview is valid and the command can reuse the result when OK is hit. This property should be ignored for all events besides the executePreview event. |
| [objectType](CommandEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [terminationReason](CommandEventArgs_terminationReason.htm) | Gets the termination reason of the command. It's only valid on the destroy event. |

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