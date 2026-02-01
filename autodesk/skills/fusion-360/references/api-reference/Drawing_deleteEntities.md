# Drawing.deleteEntities Method

Parent Object: [Drawing](Drawing.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/Drawing.h>

## Description

Deletes the specified set of entities that are associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawing\_var" is a variable referencing a [Drawing](Drawing.htm) object.```` ``` returnValue = drawing_var.deleteEntities(entities) ``` ```` |

"drawing\_var" is a variable referencing a [Drawing](Drawing.htm) object. |

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

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |