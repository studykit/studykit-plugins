# Product.unitsManager Property

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

Returns the UnitsManager object associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a Product object. |

"product\_var" is a variable referencing a Product object. ```` ``` #include <Core/Application/Product.h>  // Get the value of the property. Ptr<UnitsManager> propertyValue = product_var->unitsManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [UnitsManager](UnitsManager.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |