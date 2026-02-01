# ObjectCollection.removeByIndex Method

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

Function that removes an item from the list. Will fail if the list is read only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.```` ``` returnValue = objectCollection_var.removeByIndex(index) ``` ```` |

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the removal was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item to remove from the collection. The first item has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |