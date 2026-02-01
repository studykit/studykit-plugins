# UnitsManager.product Property

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Returns the parent Product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a UnitsManager object. |

"unitsManager\_var" is a variable referencing a UnitsManager object. ```` ``` #include <Core/Application/UnitsManager.h>  // Get the value of the property. Ptr<Product> propertyValue = unitsManager_var->product(); ``` ```` |

## Property Value

This is a read only property whose value is a [Product](Product.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |