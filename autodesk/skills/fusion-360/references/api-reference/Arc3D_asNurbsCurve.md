# Arc3D.asNurbsCurve Property

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Returns a NURBS curve that is geometrically identical to the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an Arc3D object. |

"arc3D\_var" is a variable referencing an Arc3D object. ```` ``` #include <Core/Geometry/Arc3D.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = arc3D_var->asNurbsCurve(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |