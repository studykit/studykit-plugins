# RectangularPatternConstraintInput.entities Property

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Gets and sets the entities to pattern. Sketch points and curves are valid entities to pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. |

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraintInput.h>  // Get the value of the property. std::vector<Ptr<SketchEntity>> propertyValue = rectangularPatternConstraintInput_var->entities();  // Set the value of the property, where value_var is a SketchEntity. bool returnValue = rectangularPatternConstraintInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [SketchEntity](SketchEntity.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |