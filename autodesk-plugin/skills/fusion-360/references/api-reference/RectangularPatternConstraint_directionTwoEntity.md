# RectangularPatternConstraint.directionTwoEntity Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Gets and sets the entity that defines the second direction of the pattern. This can be null which indicates to use the default direction, which is perpendicular to direction one. The directionOneEntity property must be set before setting this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = rectangularPatternConstraint_var->directionTwoEntity();  // Set the value of the property, where value_var is a SketchLine. bool returnValue = rectangularPatternConstraint_var->directionTwoEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |