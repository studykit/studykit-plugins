# DistanceAndAngleChamferTypeDefinition.angle Property

Parent Object: [DistanceAndAngleChamferTypeDefinition](DistanceAndAngleChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>

## Description

Returns the parameter controlling the angle. You can edit the angle by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object. |

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = distanceAndAngleChamferTypeDefinition_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |