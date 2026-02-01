# EqualDistanceChamferTypeDefinition.parentFeature Property

Parent Object: [EqualDistanceChamferTypeDefinition](EqualDistanceChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EqualDistanceChamferTypeDefinition.h>

## Description

Returns the feature that owns this chamfer type definition

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalDistanceChamferTypeDefinition\_var" is a variable referencing an EqualDistanceChamferTypeDefinition object. |

"equalDistanceChamferTypeDefinition\_var" is a variable referencing an EqualDistanceChamferTypeDefinition object. ```` ``` #include <Fusion/Features/EqualDistanceChamferTypeDefinition.h>  // Get the value of the property. Ptr<ChamferFeature> propertyValue = equalDistanceChamferTypeDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferFeature](ChamferFeature.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |