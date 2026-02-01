# RenderEvent.isValid Property

Parent Object: [RenderEvent](RenderEvent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEvent\_var" is a variable referencing a RenderEvent object. |

"renderEvent\_var" is a variable referencing a RenderEvent object. ```` ``` #include <Fusion/Render/RenderEvent.h>  // Get the value of the property. boolean propertyValue = renderEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |