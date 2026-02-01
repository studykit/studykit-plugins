# ObjectCollection.item Method

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

Function that returns the specified object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.```` ``` returnValue = objectCollection_var.item(index) ``` ```` |

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm) | Returns the specified item or null if an invalid index was specified. |

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