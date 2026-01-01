# SetupEventHandler.notify Method

Parent Object: [SetupEventHandler](SetupEventHandler.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEventHandler.h>

## Description

The function called by CAM when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEventHandler\_var" is a variable referencing a [SetupEventHandler](SetupEventHandler.htm) object.```` ``` returnValue = setupEventHandler_var.notify(eventArgs) ``` ```` |

"setupEventHandler\_var" is a variable referencing a [SetupEventHandler](SetupEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [SetupEventArgs](SetupEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |