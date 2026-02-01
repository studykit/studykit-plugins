# ConstructionPlane.geometry Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Returns a plane that represents the position and orientation of the construction plane. This geometry is defined in the AssemblyContext of this ConstructionPlane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. Ptr<Plane> propertyValue = constructionPlane_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [Plane](Plane.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |