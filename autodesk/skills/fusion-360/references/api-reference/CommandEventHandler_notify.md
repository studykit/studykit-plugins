# CommandEventHandler.notify Method

Parent Object: [CommandEventHandler](CommandEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventHandler\_var" is a variable referencing a [CommandEventHandler](CommandEventHandler.htm) object.```` ``` returnValue = commandEventHandler_var.notify(eventArgs) ``` ```` |

"commandEventHandler\_var" is a variable referencing a [CommandEventHandler](CommandEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [CommandEventArgs](CommandEventArgs.htm) | The arguments object with details about this event and the firing CommandEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |