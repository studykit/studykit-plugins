# CommandCreatedEventHandler.notify Method

Parent Object: [CommandCreatedEventHandler](CommandCreatedEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEventHandler\_var" is a variable referencing a [CommandCreatedEventHandler](CommandCreatedEventHandler.htm) object.```` ``` returnValue = commandCreatedEventHandler_var.notify(eventArgs) ``` ```` |

"commandCreatedEventHandler\_var" is a variable referencing a [CommandCreatedEventHandler](CommandCreatedEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [CommandCreatedEventArgs](CommandCreatedEventArgs.htm) | The arguments object with details about this event and the firing CommandEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |