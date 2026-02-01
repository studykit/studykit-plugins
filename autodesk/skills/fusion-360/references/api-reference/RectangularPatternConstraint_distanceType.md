# RectangularPatternConstraint.distanceType Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Gets and sets how the distance between elements is computed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. PatternDistanceType propertyValue = rectangularPatternConstraint_var->distanceType();  // Set the value of the property, where value_var is a PatternDistanceType. bool returnValue = rectangularPatternConstraint_var->distanceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternDistanceType](PatternDistanceType.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |