# RenderEnvironments.isValid Property

Parent Object: [RenderEnvironments](RenderEnvironments.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEnvironments\_var" is a variable referencing a RenderEnvironments object. |

"renderEnvironments\_var" is a variable referencing a RenderEnvironments object. ```` ``` #include <Fusion/Render/RenderEnvironments.h>  // Get the value of the property. boolean propertyValue = renderEnvironments_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |