# TimelineGroup.reorder Method

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Reorders this object to the position specified. The default value of -1 indicates the end of the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.  ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Uses no optional arguments. returnValue = timelineGroup_var->reorder();  // Uses optional arguments. returnValue = timelineGroup_var->reorder(beforeIndex); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the reorder operation was successful This method will fail and return false if this is a timelineGroup object and the group is expanded. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| beforeIndex | integer | The index number of the position in the timeline to place this object before   This is an optional argument whose default value is -1. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |