# WebRequestEventHandler.notify Method

Parent Object: [WebRequestEventHandler](WebRequestEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEventHandler\_var" is a variable referencing a [WebRequestEventHandler](WebRequestEventHandler.htm) object.```` ``` returnValue = webRequestEventHandler_var.notify(eventArgs) ``` ```` |

"webRequestEventHandler\_var" is a variable referencing a [WebRequestEventHandler](WebRequestEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [WebRequestEventArgs](WebRequestEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |