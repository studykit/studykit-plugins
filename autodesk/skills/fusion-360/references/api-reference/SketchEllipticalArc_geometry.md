# SketchEllipticalArc.geometry Property

Parent Object: [SketchEllipticalArc](SketchEllipticalArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

Returns the transient geometry of the elliptical arc which provides geometric information about the elliptical arc. The returned geometry is always in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. |

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. ```` ``` #include <Fusion/Sketch/SketchEllipticalArc.h>  // Get the value of the property. Ptr<EllipticalArc3D> propertyValue = sketchEllipticalArc_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is an [EllipticalArc3D](EllipticalArc3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |