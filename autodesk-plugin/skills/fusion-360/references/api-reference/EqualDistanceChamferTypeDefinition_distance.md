# EqualDistanceChamferTypeDefinition.distance Property

Parent Object: [EqualDistanceChamferTypeDefinition](EqualDistanceChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EqualDistanceChamferTypeDefinition.h>

## Description

Returns the parameter controlling the distance. You can edit the distance by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalDistanceChamferTypeDefinition\_var" is a variable referencing an EqualDistanceChamferTypeDefinition object. |

"equalDistanceChamferTypeDefinition\_var" is a variable referencing an EqualDistanceChamferTypeDefinition object. ```` ``` #include <Fusion/Features/EqualDistanceChamferTypeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = equalDistanceChamferTypeDefinition_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |