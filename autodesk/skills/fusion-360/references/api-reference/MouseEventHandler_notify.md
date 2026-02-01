# MouseEventHandler.notify Method

Parent Object: [MouseEventHandler](MouseEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventHandler\_var" is a variable referencing a [MouseEventHandler](MouseEventHandler.htm) object.```` ``` returnValue = mouseEventHandler_var.notify(eventArgs) ``` ```` |

"mouseEventHandler\_var" is a variable referencing a [MouseEventHandler](MouseEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [MouseEventArgs](MouseEventArgs.htm) | The arguments object with details about this event and the firing MouseEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |