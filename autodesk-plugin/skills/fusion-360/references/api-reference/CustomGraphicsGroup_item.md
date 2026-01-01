# CustomGraphicsGroup.item Method

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Function that returns the specified custom graphics entity within this group. This also includes any child graphics groups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object.```` ``` returnValue = customGraphicsGroup_var.item(index) ``` ```` |

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsEntity](CustomGraphicsEntity.htm) | Returns the specified item or null if an invalid index was specified. |

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