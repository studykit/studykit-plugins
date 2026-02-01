# SketchEllipse.majorAxisLine Property

Parent Object: [SketchEllipse](SketchEllipse.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipse.h>

## Description

Returns the sketch line associated with the ellipse that lies along the major axis. This can return null in the case where the line has been deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. |

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. ```` ``` #include <Fusion/Sketch/SketchEllipse.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = sketchEllipse_var->majorAxisLine(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |