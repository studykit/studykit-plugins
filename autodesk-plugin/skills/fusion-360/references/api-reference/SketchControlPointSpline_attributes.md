# SketchControlPointSpline.attributes Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. Ptr<Attributes> propertyValue = sketchControlPointSpline_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |