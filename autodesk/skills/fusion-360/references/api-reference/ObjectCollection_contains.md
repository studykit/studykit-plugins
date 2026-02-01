# ObjectCollection.contains Method

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

Returns whether the specified object exists within the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.```` ``` returnValue = objectCollection_var.contains(item) ``` ```` |

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the specified item is found in the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| item | [Base](Base.htm) | The item to look for in the collection. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |