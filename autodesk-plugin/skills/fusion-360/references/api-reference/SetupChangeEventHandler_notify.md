# SetupChangeEventHandler.notify Method

Parent Object: [SetupChangeEventHandler](SetupChangeEventHandler.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventHandler.h>

## Description

The function called by CAM when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEventHandler\_var" is a variable referencing a [SetupChangeEventHandler](SetupChangeEventHandler.htm) object.```` ``` returnValue = setupChangeEventHandler_var.notify(eventArgs) ``` ```` |

"setupChangeEventHandler\_var" is a variable referencing a [SetupChangeEventHandler](SetupChangeEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [SetupChangeEventArgs](SetupChangeEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |