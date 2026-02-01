# RectangularPatternConstraint.entities Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Gets and sets the entities that are patterned. Sketch points and curves are valid entities to pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. std::vector<Ptr<SketchEntity>> propertyValue = rectangularPatternConstraint_var->entities();  // Set the value of the property, where value_var is a SketchEntity. bool returnValue = rectangularPatternConstraint_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [SketchEntity](SketchEntity.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |