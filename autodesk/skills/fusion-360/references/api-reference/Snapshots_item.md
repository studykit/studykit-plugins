# Snapshots.item Method

Parent Object: [Snapshots](Snapshots.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Snapshots.h>

## Description

Function that returns the specified snapshot in the collection using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"snapshots\_var" is a variable referencing a [Snapshots](Snapshots.htm) object.```` ``` returnValue = snapshots_var.item(index) ``` ```` |

"snapshots\_var" is a variable referencing a [Snapshots](Snapshots.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Snapshot](Snapshot.htm) | Returns the specified item or null if an invalid index was specified. |

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