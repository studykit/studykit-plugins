# RenderEventArgs.isValid Property

Parent Object: [RenderEventArgs](RenderEventArgs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. |

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. ```` ``` #include <Fusion/Render/RenderEventArgs.h>  // Get the value of the property. boolean propertyValue = renderEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |