# RenderEvent.add Method

Parent Object: [RenderEvent](RenderEvent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEvent\_var" is a variable referencing a [RenderEvent](RenderEvent.htm) object.```` ``` returnValue = renderEvent_var.add(handler) ``` ```` |

"renderEvent\_var" is a variable referencing a [RenderEvent](RenderEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [RenderEventHandler](RenderEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |