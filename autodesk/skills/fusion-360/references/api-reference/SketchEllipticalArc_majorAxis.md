# SketchEllipticalArc.majorAxis Property

Parent Object: [SketchEllipticalArc](SketchEllipticalArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

Gets and sets the major axis direction of the elliptical arc. Changing the axis is limited by any constraints that might exist on the elliptical arc. Setting the axis can fail in cases where the direction is fully defined through constraints.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. |

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. ```` ``` #include <Fusion/Sketch/SketchEllipticalArc.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = sketchEllipticalArc_var->majorAxis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = sketchEllipticalArc_var->majorAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |