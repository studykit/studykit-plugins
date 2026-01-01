# DocumentEventHandler.notify Method

Parent Object: [DocumentEventHandler](DocumentEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventHandler\_var" is a variable referencing a [DocumentEventHandler](DocumentEventHandler.htm) object.```` ``` returnValue = documentEventHandler_var.notify(eventArgs) ``` ```` |

"documentEventHandler\_var" is a variable referencing a [DocumentEventHandler](DocumentEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [DocumentEventArgs](DocumentEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |