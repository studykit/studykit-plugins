# Product.deleteEntities Method

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

Deletes the specified set of entities that are associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a [Product](Product.htm) object.```` ``` returnValue = product_var.deleteEntities(entities) ``` ```` |

"product\_var" is a variable referencing a [Product](Product.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns True if any of the entities provided in the list were deleted. If entities were specified that can't be deleted or aren't owned by this product, they are ignored. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entities | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the list of entities to delete. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |