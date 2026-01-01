# DataEventHandler.notify Method

Parent Object: [DataEventHandler](DataEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventHandler\_var" is a variable referencing a [DataEventHandler](DataEventHandler.htm) object.```` ``` returnValue = dataEventHandler_var.notify(eventArgs) ``` ```` |

"dataEventHandler\_var" is a variable referencing a [DataEventHandler](DataEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [DataEventArgs](DataEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |