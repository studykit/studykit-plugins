# Line2D.isValid Property

Parent Object: [Line2D](Line2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line2D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line2D\_var" is a variable referencing a Line2D object. |

"line2D\_var" is a variable referencing a Line2D object. ```` ``` #include <Core/Geometry/Line2D.h>  // Get the value of the property. boolean propertyValue = line2D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |