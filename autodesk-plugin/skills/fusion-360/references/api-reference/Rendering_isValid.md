# Rendering.isValid Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. boolean propertyValue = rendering_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |