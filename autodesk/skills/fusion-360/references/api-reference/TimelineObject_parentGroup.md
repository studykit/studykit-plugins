# TimelineObject.parentGroup Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Returns the parent group, if this object is part of a group. Returns null if this object is not part of a group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object. |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. Ptr<TimelineGroup> propertyValue = timelineObject_var->parentGroup(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineGroup](TimelineGroup.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |