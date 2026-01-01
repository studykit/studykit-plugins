# HttpEventHandler.notify Method

Parent Object: [HttpEventHandler](HttpEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEventHandler\_var" is a variable referencing a [HttpEventHandler](HttpEventHandler.htm) object.```` ``` returnValue = httpEventHandler_var.notify(eventArgs) ``` ```` |

"httpEventHandler\_var" is a variable referencing a [HttpEventHandler](HttpEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [HttpEventArgs](HttpEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |