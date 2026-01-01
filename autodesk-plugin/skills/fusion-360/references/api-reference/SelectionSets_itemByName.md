# SelectionSets.itemByName Method

Parent Object: [SelectionSets](SelectionSets.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSets.h>

## Description

Returns the specified SelectionSet object using the name of the selection set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSets\_var" is a variable referencing a [SelectionSets](SelectionSets.htm) object.```` ``` returnValue = selectionSets_var.itemByName(name) ``` ```` |

"selectionSets\_var" is a variable referencing a [SelectionSets](SelectionSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SelectionSet](SelectionSet.htm) | Returns the specified SelectionSet object or null if no SelectionSet object exists with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the SelectionSet object to return. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |