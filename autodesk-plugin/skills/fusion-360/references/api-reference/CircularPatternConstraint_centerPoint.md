# CircularPatternConstraint.centerPoint Property

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

Gets and sets the sketch point that defines the center of the pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. |

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraint.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = circularPatternConstraint_var->centerPoint();  // Set the value of the property, where value_var is a SketchPoint. bool returnValue = circularPatternConstraint_var->centerPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |