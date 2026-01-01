# ObjectCollection.add Method

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

Adds an object to the end of the collection. Duplicates can be added to the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.```` ``` returnValue = objectCollection_var.add(item) ``` ```` |

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns false if the item was not added. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| item | [Base](Base.htm) | The item to add to the list. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |