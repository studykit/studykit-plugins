# FusionUnitsManager.product Property

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Returns the parent Product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. |

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Get the value of the property. Ptr<Product> propertyValue = fusionUnitsManager_var->product(); ``` ```` |

## Property Value

This is a read only property whose value is a [Product](Product.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |