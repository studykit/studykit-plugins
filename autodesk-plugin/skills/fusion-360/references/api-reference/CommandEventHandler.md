# CommandEventHandler Object

Derived from: [EventHandler](EventHandler.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventHandler.h>

## Description

An command event handler base class that a client derives from to handle events triggered by a CommandEvent. A client implemented instance of this class can be added to a CommandEvent to receive these event notifications.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [notify](CommandEventHandler_notify.htm) | This notify member is called when an event is triggered from any event that this handler has been added to. |

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