# ConstructionAxis.geometry Property

Parent Object: [ConstructionAxis](ConstructionAxis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxis.h>

## Description

Returns an infinite line that represents the position and orientation of the construction axis. This geometry is defined in the AssemblyContext of this ConstructionAxis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. |

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. ```` ``` #include <Fusion/Construction/ConstructionAxis.h>  // Get the value of the property. Ptr<InfiniteLine3D> propertyValue = constructionAxis_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is an [InfiniteLine3D](InfiniteLine3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |