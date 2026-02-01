# SketchArc.geometry Property

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

Returns the transient geometry of the arc which provides geometric information about the arc. The returned geometry is always in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a SketchArc object. |

"sketchArc\_var" is a variable referencing a SketchArc object. ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Get the value of the property. Ptr<Arc3D> propertyValue = sketchArc_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is an [Arc3D](Arc3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |