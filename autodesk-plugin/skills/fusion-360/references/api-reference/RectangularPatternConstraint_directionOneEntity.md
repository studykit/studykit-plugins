# RectangularPatternConstraint.directionOneEntity Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Gets and sets the entity that defined the first direction of the pattern. This can be null which indicates to use the default which is the X-axis of the sketch. Setting this property to null will automatically clear directionTwoEntity, if it has been set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = rectangularPatternConstraint_var->directionOneEntity();  // Set the value of the property, where value_var is a SketchLine. bool returnValue = rectangularPatternConstraint_var->directionOneEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |