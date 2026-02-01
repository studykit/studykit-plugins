# TimelineObject.index Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Returns the position of this item within the timeline where the first item has an index of 0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object.  ```` ``` # Get the value of the property. propertyValue = timelineObject_var.index ``` ```` |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. integer propertyValue = timelineObject_var->index(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |