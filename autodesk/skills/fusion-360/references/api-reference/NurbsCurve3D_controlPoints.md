# NurbsCurve3D.controlPoints Property

Parent Object: [NurbsCurve3D](NurbsCurve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Returns an array of Point3D objects that define the control points of the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve3D\_var" is a variable referencing a NurbsCurve3D object. |

"nurbsCurve3D\_var" is a variable referencing a NurbsCurve3D object. ```` ``` #include <Core/Geometry/NurbsCurve3D.h>  // Get the value of the property. std::vector<Ptr<Point3D>> propertyValue = nurbsCurve3D_var->controlPoints(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |