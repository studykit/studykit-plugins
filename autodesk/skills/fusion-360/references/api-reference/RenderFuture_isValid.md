# RenderFuture.isValid Property

Parent Object: [RenderFuture](RenderFuture.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderFuture.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderFuture\_var" is a variable referencing a RenderFuture object. |

"renderFuture\_var" is a variable referencing a RenderFuture object. ```` ``` #include <Fusion/Render/RenderFuture.h>  // Get the value of the property. boolean propertyValue = renderFuture_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |