# Products.item Method

Parent Object: [Products](Products.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Products.h>

## Description

Function that returns the specified product using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"products\_var" is a variable referencing a [Products](Products.htm) object.```` ``` returnValue = products_var.item(index) ``` ```` |

"products\_var" is a variable referencing a [Products](Products.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Product](Product.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |