# ConstructionPlane.displayBounds Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Gets and sets the display size of the construction plane. The bounding box defines the min and max corners of the plane as defined in the 2D space of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. Ptr<BoundingBox2D> propertyValue = constructionPlane_var->displayBounds();  // Set the value of the property, where value_var is a BoundingBox2D. bool returnValue = constructionPlane_var->displayBounds(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BoundingBox2D](BoundingBox2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |