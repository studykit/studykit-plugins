# DistanceExtentDefinition.distance Property

Parent Object: [DistanceExtentDefinition](DistanceExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceExtentDefinition.h>

## Description

Returns the parameter controlling the distance. You can edit the distance by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object. |

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object. ```` ``` #include <Fusion/Features/DistanceExtentDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = distanceExtentDefinition_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |