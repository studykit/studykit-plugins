# TimelineGroups.item Method

Parent Object: [TimelineGroups](TimelineGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroups.h>

## Description

Function that returns the specified timeline group using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroups\_var" is a variable referencing a [TimelineGroups](TimelineGroups.htm) object.```` ``` returnValue = timelineGroups_var.item(index) ``` ```` |

"timelineGroups\_var" is a variable referencing a [TimelineGroups](TimelineGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TimelineGroup](TimelineGroup.htm) | Returns the specified item or null if an invalid index was specified. |

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