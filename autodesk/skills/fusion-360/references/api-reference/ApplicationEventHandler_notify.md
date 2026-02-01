# ApplicationEventHandler.notify Method

Parent Object: [ApplicationEventHandler](ApplicationEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEventHandler\_var" is a variable referencing an [ApplicationEventHandler](ApplicationEventHandler.htm) object.```` ``` returnValue = applicationEventHandler_var.notify(eventArgs) ``` ```` |

"applicationEventHandler\_var" is a variable referencing an [ApplicationEventHandler](ApplicationEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [ApplicationEventArgs](ApplicationEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |