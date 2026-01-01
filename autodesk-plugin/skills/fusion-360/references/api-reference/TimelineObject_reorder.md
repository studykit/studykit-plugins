# TimelineObject.reorder Method

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Reorders this object to the position specified. The default value of -1 indicates the end of the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a [TimelineObject](TimelineObject.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"timelineObject\_var" is a variable referencing a [TimelineObject](TimelineObject.htm) object.  ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Uses no optional arguments. returnValue = timelineObject_var->reorder();  // Uses optional arguments. returnValue = timelineObject_var->reorder(beforeIndex); ``` ```` |

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