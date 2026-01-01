# BRepBody.orientedMinimumBoundingBox Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns an oriented bounding box of the body that is best oriented to tightly fit the body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object. |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. Ptr<OrientedBoundingBox3D> propertyValue = bRepBody_var->orientedMinimumBoundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |