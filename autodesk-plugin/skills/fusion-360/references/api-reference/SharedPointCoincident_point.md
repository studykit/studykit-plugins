# SharedPointCoincident.point Property

Parent Object: [SharedPointCoincident](SharedPointCoincident.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SharedPointCoincident.h>

## Description

Returns the sketch point that the sketch curves are connected to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object. |

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object. ```` ``` #include <Fusion/Sketch/SharedPointCoincident.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = sharedPointCoincident_var->point(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |