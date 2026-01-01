# RenderEvent.remove Method

Parent Object: [RenderEvent](RenderEvent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEvent\_var" is a variable referencing a [RenderEvent](RenderEvent.htm) object.```` ``` returnValue = renderEvent_var.remove(handler) ``` ```` |

"renderEvent\_var" is a variable referencing a [RenderEvent](RenderEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [RenderEventHandler](RenderEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |