# ObjectCollection.find Method

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

Finds the specified component in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"objectCollection\_var" is a variable referencing an [ObjectCollection](ObjectCollection.htm) object.  ```` ``` #include <Core/Application/ObjectCollection.h>  // Uses no optional arguments. returnValue = objectCollection_var->find(item);  // Uses optional arguments. returnValue = objectCollection_var->find(item, startIndex); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| integer | Returns the index of the found item. If not found, -1 is returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| item | [Base](Base.htm) | The item to search for within the collection. |
| startIndex | uinteger | The index to begin the search.   This is an optional argument whose default value is 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |