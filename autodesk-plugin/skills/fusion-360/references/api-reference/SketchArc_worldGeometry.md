# SketchArc.worldGeometry Property

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

Returns an Arc3D object which provides geometric information in world space. The returned geometry takes into account the assembly context and the position of the sketch in it's parent component, which means the geometry will be returned in the root component space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a SketchArc object. |

"sketchArc\_var" is a variable referencing a SketchArc object. ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Get the value of the property. Ptr<Arc3D> propertyValue = sketchArc_var->worldGeometry(); ``` ```` |

## Property Value

This is a read only property whose value is an [Arc3D](Arc3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |