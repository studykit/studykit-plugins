# DocumentEvent.remove Method

Parent Object: [DocumentEvent](DocumentEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEvent\_var" is a variable referencing a [DocumentEvent](DocumentEvent.htm) object.```` ``` returnValue = documentEvent_var.remove(handler) ``` ```` |

"documentEvent\_var" is a variable referencing a [DocumentEvent](DocumentEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [DocumentEventHandler](DocumentEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |