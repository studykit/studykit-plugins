# AllExtentDefinition.direction Property

Parent Object: [AllExtentDefinition](AllExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AllExtentDefinition.h>

## Description

Gets and sets the direction of the extent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"allExtentDefinition\_var" is a variable referencing an AllExtentDefinition object. |

"allExtentDefinition\_var" is a variable referencing an AllExtentDefinition object. ```` ``` #include <Fusion/Features/AllExtentDefinition.h>  // Get the value of the property. ExtentDirections propertyValue = allExtentDefinition_var->direction();  // Set the value of the property, where value_var is an ExtentDirections. bool returnValue = allExtentDefinition_var->direction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtentDirections](ExtentDirections.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |