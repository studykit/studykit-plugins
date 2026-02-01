# DistanceAndAngleChamferTypeDefinition.distance Property

Parent Object: [DistanceAndAngleChamferTypeDefinition](DistanceAndAngleChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>

## Description

Returns the parameter controlling the distance. You can edit the distance by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object. |

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = distanceAndAngleChamferTypeDefinition_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |