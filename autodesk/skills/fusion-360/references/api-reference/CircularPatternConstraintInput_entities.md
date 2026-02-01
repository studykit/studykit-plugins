# CircularPatternConstraintInput.entities Property

Parent Object: [CircularPatternConstraintInput](CircularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraintInput.h>

## Description

Gets and sets the entities to pattern. Sketch points and curves are valid entities to pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. |

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraintInput.h>  // Get the value of the property. std::vector<Ptr<SketchEntity>> propertyValue = circularPatternConstraintInput_var->entities();  // Set the value of the property, where value_var is a SketchEntity. bool returnValue = circularPatternConstraintInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [SketchEntity](SketchEntity.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |