# BossFeatureSideInput.ribRotation Property

Parent Object: [BossFeatureSideInput](BossFeatureSideInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

Get or set rotation angle of the first rib from the reference vector. Reference vector is X-axis of the parent sketch from selected sketch point(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. |

"bossFeatureSideInput\_var" is a variable referencing a BossFeatureSideInput object. ```` ``` #include <Fusion/Plastic/BossFeatureSideInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = bossFeatureSideInput_var->ribRotation();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = bossFeatureSideInput_var->ribRotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |