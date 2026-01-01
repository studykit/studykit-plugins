# CustomGraphicsGroups.item Method

Parent Object: [CustomGraphicsGroups](CustomGraphicsGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroups.h>

## Description

Function that returns the specified graphics group using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroups\_var" is a variable referencing a [CustomGraphicsGroups](CustomGraphicsGroups.htm) object.```` ``` returnValue = customGraphicsGroups_var.item(index) ``` ```` |

"customGraphicsGroups\_var" is a variable referencing a [CustomGraphicsGroups](CustomGraphicsGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsGroup](CustomGraphicsGroup.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |