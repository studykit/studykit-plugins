# ChamferTypeDefinition.parentFeature Property

Parent Object: [ChamferTypeDefinition](ChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferTypeDefinition.h>

## Description

Returns the feature that owns this chamfer type definition

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferTypeDefinition\_var" is a variable referencing a ChamferTypeDefinition object. |

"chamferTypeDefinition\_var" is a variable referencing a ChamferTypeDefinition object. ```` ``` #include <Fusion/Features/ChamferTypeDefinition.h>  // Get the value of the property. Ptr<ChamferFeature> propertyValue = chamferTypeDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferFeature](ChamferFeature.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |