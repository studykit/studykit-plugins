# TwoSidesToExtentDefinition.matchShape Property

Parent Object: [TwoSidesToExtentDefinition](TwoSidesToExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoSidesToExtentDefinition.h>

## Description

Gets and sets whether the toEntity is extended to fully intersect the extrusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoSidesToExtentDefinition\_var" is a variable referencing a TwoSidesToExtentDefinition object. |

"twoSidesToExtentDefinition\_var" is a variable referencing a TwoSidesToExtentDefinition object. ```` ``` #include <Fusion/Features/TwoSidesToExtentDefinition.h>  // Get the value of the property. boolean propertyValue = twoSidesToExtentDefinition_var->matchShape();  // Set the value of the property, where value_var is a boolean. bool returnValue = twoSidesToExtentDefinition_var->matchShape(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |