# Product.parentDocument Property

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

Returns the parent Document object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a Product object. |

"product\_var" is a variable referencing a Product object. ```` ``` #include <Core/Application/Product.h>  // Get the value of the property. Ptr<Document> propertyValue = product_var->parentDocument(); ``` ```` |

## Property Value

This is a read only property whose value is a [Document](Document.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |