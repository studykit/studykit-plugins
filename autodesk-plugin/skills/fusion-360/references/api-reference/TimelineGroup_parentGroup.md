# TimelineGroup.parentGroup Property

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Returns the parent group, if this object is part of a group. Returns null if this object is not part of a group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a TimelineGroup object. |

"timelineGroup\_var" is a variable referencing a TimelineGroup object. ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Get the value of the property. Ptr<TimelineGroup> propertyValue = timelineGroup_var->parentGroup(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineGroup](TimelineGroup.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |