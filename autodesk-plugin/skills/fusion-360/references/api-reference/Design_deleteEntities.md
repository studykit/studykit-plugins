# Design.deleteEntities Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Deletes the specified set of entities that are associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` returnValue = design_var.deleteEntities(entities) ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object. |

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