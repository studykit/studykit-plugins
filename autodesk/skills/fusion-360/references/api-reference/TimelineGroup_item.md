# TimelineGroup.item Method

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Function that returns the specified timeline object within the group using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.```` ``` returnValue = timelineGroup_var.item(index) ``` ```` |

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TimelineObject](TimelineObject.htm) | Returns the specified item or null if an invalid index was specified. |

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