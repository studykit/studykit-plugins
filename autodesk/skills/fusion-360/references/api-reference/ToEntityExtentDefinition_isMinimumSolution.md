# ToEntityExtentDefinition.isMinimumSolution Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

Gets and sets if the minimum or maximum solution is calculated. This is only used when the input entity is a body and defines if the extrusion to go to the near side (minimum solution) of the body or the far side. When a new ToEntityExtentDefinition object is created, this property defaults to True.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. boolean propertyValue = toEntityExtentDefinition_var->isMinimumSolution();  // Set the value of the property, where value_var is a boolean. bool returnValue = toEntityExtentDefinition_var->isMinimumSolution(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |