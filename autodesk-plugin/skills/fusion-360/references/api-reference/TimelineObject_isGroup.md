# TimelineObject.isGroup Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Indicates if this TimelineObject represents a group. If True you can operate on this object as a TimelineGroup object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object. |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. boolean propertyValue = timelineObject_var->isGroup(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |