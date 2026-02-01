# RectangularPatternConstraintInput.directionOneEntity Property

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Defines the first direction of the pattern. This can be null which indicates to use the default which is the X-axis of the sketch. Setting this property to null will automatically clear directionTwoEntity, if it has been set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. |

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraintInput.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = rectangularPatternConstraintInput_var->directionOneEntity();  // Set the value of the property, where value_var is a SketchLine. bool returnValue = rectangularPatternConstraintInput_var->directionOneEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |