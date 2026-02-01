# DecalInput.targetBaseFeature Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object.  ```` ``` # Get the value of the property. propertyValue = decalInput_var.targetBaseFeature  # Set the value of the property. decalInput_var.targetBaseFeature = propertyValue ``` ```` |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. Ptr<BaseFeature> propertyValue = decalInput_var->targetBaseFeature();  // Set the value of the property, where value_var is a BaseFeature. bool returnValue = decalInput_var->targetBaseFeature(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BaseFeature](BaseFeature.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |