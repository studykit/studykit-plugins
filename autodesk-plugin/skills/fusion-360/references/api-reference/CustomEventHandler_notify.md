# CustomEventHandler.notify Method

Parent Object: [CustomEventHandler](CustomEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEventHandler\_var" is a variable referencing a [CustomEventHandler](CustomEventHandler.htm) object.```` ``` returnValue = customEventHandler_var.notify(eventArgs) ``` ```` |

"customEventHandler\_var" is a variable referencing a [CustomEventHandler](CustomEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [CustomEventArgs](CustomEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |