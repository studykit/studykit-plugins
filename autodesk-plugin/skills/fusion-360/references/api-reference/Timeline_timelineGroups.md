# Timeline.timelineGroups Property

Parent Object: [Timeline](Timeline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Timeline.h>

## Description

Returns the collection of groups within the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timeline\_var" is a variable referencing a Timeline object. |

"timeline\_var" is a variable referencing a Timeline object. ```` ``` #include <Fusion/Fusion/Timeline.h>  // Get the value of the property. Ptr<TimelineGroups> propertyValue = timeline_var->timelineGroups(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineGroups](TimelineGroups.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |