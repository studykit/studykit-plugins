# Features.item Method

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Function that returns the specified feature using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a [Features](Features.htm) object.```` ``` returnValue = features_var.item(index) ``` ```` |

"features\_var" is a variable referencing a [Features](Features.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Feature](Feature.htm) | Returns the specified item or null if an invalid index was specified. |

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