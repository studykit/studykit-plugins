# Viewport.isValid Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. boolean propertyValue = viewport_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |