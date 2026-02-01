# SketchFixedSpline.referencedEntity Property

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object. |

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object. ```` ``` #include <Fusion/Sketch/SketchFixedSpline.h>  // Get the value of the property. Ptr<Base> propertyValue = sketchFixedSpline_var->referencedEntity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |