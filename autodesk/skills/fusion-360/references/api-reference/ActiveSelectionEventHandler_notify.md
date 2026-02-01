# ActiveSelectionEventHandler.notify Method

Parent Object: [ActiveSelectionEventHandler](ActiveSelectionEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEventHandler\_var" is a variable referencing an [ActiveSelectionEventHandler](ActiveSelectionEventHandler.htm) object.```` ``` returnValue = activeSelectionEventHandler_var.notify(eventArgs) ``` ```` |

"activeSelectionEventHandler\_var" is a variable referencing an [ActiveSelectionEventHandler](ActiveSelectionEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |