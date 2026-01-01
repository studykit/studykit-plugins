# KeyboardEventHandler.notify Method

Parent Object: [KeyboardEventHandler](KeyboardEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventHandler\_var" is a variable referencing a [KeyboardEventHandler](KeyboardEventHandler.htm) object.```` ``` returnValue = keyboardEventHandler_var.notify(eventArgs) ``` ```` |

"keyboardEventHandler\_var" is a variable referencing a [KeyboardEventHandler](KeyboardEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [KeyboardEventArgs](KeyboardEventArgs.htm) | The arguments object with details about this event and the firing KeyboardEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |