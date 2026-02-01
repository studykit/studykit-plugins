# HTMLEvent.remove Method

Parent Object: [HTMLEvent](HTMLEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEvent\_var" is a variable referencing a [HTMLEvent](HTMLEvent.htm) object.```` ``` returnValue = hTMLEvent_var.remove(handler) ``` ```` |

"hTMLEvent\_var" is a variable referencing a [HTMLEvent](HTMLEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [HTMLEventHandler](HTMLEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |