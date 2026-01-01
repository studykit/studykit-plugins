# Ellipse3D.asNurbsCurve Property

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Returns a NURBS curve that is geometrically identical to the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse3D\_var" is a variable referencing an Ellipse3D object. |

"ellipse3D\_var" is a variable referencing an Ellipse3D object. ```` ``` #include <Core/Geometry/Ellipse3D.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = ellipse3D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |