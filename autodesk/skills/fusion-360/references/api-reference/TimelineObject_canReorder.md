# TimelineObject.canReorder Method

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Checks to see if this object can be reordered to the specified position. The default value of -1 indicates the end of the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a [TimelineObject](TimelineObject.htm) object.```` ``` # Uses no optional arguments. returnValue = timelineObject_var.canReorder()  # Uses optional arguments. returnValue = timelineObject_var.canReorder(beforeIndex) ``` ```` |

"timelineObject\_var" is a variable referencing a [TimelineObject](TimelineObject.htm) object.  ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Uses no optional arguments. returnValue = timelineObject_var->canReorder();  // Uses optional arguments. returnValue = timelineObject_var->canReorder(beforeIndex); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the object can be reordered to the specified position |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| beforeIndex | integer | The index number of the position in the timeline to check   This is an optional argument whose default value is -1. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |