# TimelineGroup.index Property

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Returns the position of this item within the timeline where the first item has an index of 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a TimelineGroup object.  ```` ``` # Get the value of the property. propertyValue = timelineGroup_var.index ``` ```` |

"timelineGroup\_var" is a variable referencing a TimelineGroup object. ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Get the value of the property. integer propertyValue = timelineGroup_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |