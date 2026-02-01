# TimelineObject.isRolledBack Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Indicates if this item is currently not being computed because it has been rolled back.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object.  ```` ``` # Get the value of the property. propertyValue = timelineObject_var.isRolledBack ``` ```` |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. boolean propertyValue = timelineObject_var->isRolledBack(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |