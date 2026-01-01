# Product.namedViews Property

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a Product object. |

"product\_var" is a variable referencing a Product object. ```` ``` #include <Core/Application/Product.h>  // Get the value of the property. Ptr<NamedViews> propertyValue = product_var->namedViews(); ``` ```` |

## Property Value

This is a read only property whose value is a [NamedViews](NamedViews.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |