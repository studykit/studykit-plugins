# SelectionSets.item Method

Parent Object: [SelectionSets](SelectionSets.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSets.h>

## Description

Returns the specified SelectionSet object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSets\_var" is a variable referencing a [SelectionSets](SelectionSets.htm) object.```` ``` returnValue = selectionSets_var.item(index) ``` ```` |

"selectionSets\_var" is a variable referencing a [SelectionSets](SelectionSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SelectionSet](SelectionSet.htm) | Returns the specified SelectionSet or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the SelectionSet within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |