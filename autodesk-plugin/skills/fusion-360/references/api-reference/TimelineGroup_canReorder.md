# TimelineGroup.canReorder Method

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Checks to see if this object can be reordered to the specified position. The default value of -1 indicates the end of the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.```` ``` # Uses no optional arguments. returnValue = timelineGroup_var.canReorder()  # Uses optional arguments. returnValue = timelineGroup_var.canReorder(beforeIndex) ``` ```` |

"timelineGroup\_var" is a variable referencing a [TimelineGroup](TimelineGroup.htm) object.  ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Uses no optional arguments. returnValue = timelineGroup_var->canReorder();  // Uses optional arguments. returnValue = timelineGroup_var->canReorder(beforeIndex); ``` ```` |

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