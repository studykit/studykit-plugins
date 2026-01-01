# Product.productType Property

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a Product object. |

"product\_var" is a variable referencing a Product object. ```` ``` #include <Core/Application/Product.h>  // Get the value of the property. string propertyValue = product_var->productType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |