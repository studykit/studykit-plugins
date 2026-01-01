# TimelineGroup.isRolledBack Property

Parent Object: [TimelineGroup](TimelineGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroup.h>

## Description

Indicates if this item is currently not being computed because it has been rolled back.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroup\_var" is a variable referencing a TimelineGroup object.  ```` ``` # Get the value of the property. propertyValue = timelineGroup_var.isRolledBack ``` ```` |

"timelineGroup\_var" is a variable referencing a TimelineGroup object. ```` ``` #include <Fusion/Fusion/TimelineGroup.h>  // Get the value of the property. boolean propertyValue = timelineGroup_var->isRolledBack(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |