# Drawing.productType Property

Parent Object: [Drawing](Drawing.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/Drawing.h>

## Description

Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawing\_var" is a variable referencing a Drawing object. |

"drawing\_var" is a variable referencing a Drawing object. ```` ``` #include <Drawing/Drawing/Drawing.h>  // Get the value of the property. string propertyValue = drawing_var->productType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |