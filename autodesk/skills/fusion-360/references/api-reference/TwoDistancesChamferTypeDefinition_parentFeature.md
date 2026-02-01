# TwoDistancesChamferTypeDefinition.parentFeature Property

Parent Object: [TwoDistancesChamferTypeDefinition](TwoDistancesChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoDistancesChamferTypeDefinition.h>

## Description

Returns the feature that owns this chamfer type definition

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoDistancesChamferTypeDefinition\_var" is a variable referencing a TwoDistancesChamferTypeDefinition object. |

"twoDistancesChamferTypeDefinition\_var" is a variable referencing a TwoDistancesChamferTypeDefinition object. ```` ``` #include <Fusion/Features/TwoDistancesChamferTypeDefinition.h>  // Get the value of the property. Ptr<ChamferFeature> propertyValue = twoDistancesChamferTypeDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferFeature](ChamferFeature.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |