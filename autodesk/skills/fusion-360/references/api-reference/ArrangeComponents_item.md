# ArrangeComponents.item Method

Parent Object: [ArrangeComponents](ArrangeComponents.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponents.h>

## Description

Returns an ArrangeComponent object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponents\_var" is a variable referencing an [ArrangeComponents](ArrangeComponents.htm) object.```` ``` returnValue = arrangeComponents_var.item(index) ``` ```` |

"arrangeComponents\_var" is a variable referencing an [ArrangeComponents](ArrangeComponents.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeComponent](ArrangeComponent.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |