# RectangularPatternConstraint.createdEntities Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Returns an array that contains all of the sketch entities that were created as a result of the pattern. This does not contain the original entities that were used as input to the pattern. The input entities can be obtained by using the entities property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. std::vector<Ptr<SketchEntity>> propertyValue = rectangularPatternConstraint_var->createdEntities(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [SketchEntity](SketchEntity.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |