# DocumentEvent.add Method

Parent Object: [DocumentEvent](DocumentEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEvent.h>

## Description

Add a handler to be notified when the file event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEvent\_var" is a variable referencing a [DocumentEvent](DocumentEvent.htm) object.```` ``` returnValue = documentEvent_var.add(handler) ``` ```` |

"documentEvent\_var" is a variable referencing a [DocumentEvent](DocumentEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [DocumentEventHandler](DocumentEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |