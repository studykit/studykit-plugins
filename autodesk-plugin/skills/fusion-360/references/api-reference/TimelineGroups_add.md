# TimelineGroups.add Method

Parent Object: [TimelineGroups](TimelineGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroups.h>

## Description

Creates a new group within the timeline. The sequential set of items defined by the start and end indices will be included in the group. A group cannot contains another group so none of the items being grouped can be a group of this will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroups\_var" is a variable referencing a [TimelineGroups](TimelineGroups.htm) object.```` ``` returnValue = timelineGroups_var.add(startIndex, endIndex) ``` ```` |

"timelineGroups\_var" is a variable referencing a [TimelineGroups](TimelineGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TimelineGroup](TimelineGroup.htm) | Returns the created TimelineGroup object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startIndex | integer | The index of the first item in the timeline that will be added to the group. |
| endIndex | integer | The index of the last item in the timeline that will be added to the group. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |