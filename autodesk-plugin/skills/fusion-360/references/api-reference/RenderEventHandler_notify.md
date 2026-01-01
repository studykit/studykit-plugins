# RenderEventHandler.notify Method

Parent Object: [RenderEventHandler](RenderEventHandler.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEventHandler\_var" is a variable referencing a [RenderEventHandler](RenderEventHandler.htm) object.```` ``` returnValue = renderEventHandler_var.notify(eventArgs) ``` ```` |

"renderEventHandler\_var" is a variable referencing a [RenderEventHandler](RenderEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [RenderEventArgs](RenderEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |