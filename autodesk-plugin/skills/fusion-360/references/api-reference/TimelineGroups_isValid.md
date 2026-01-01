# TimelineGroups.isValid Property

Parent Object: [TimelineGroups](TimelineGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineGroups.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineGroups\_var" is a variable referencing a TimelineGroups object. |

"timelineGroups\_var" is a variable referencing a TimelineGroups object. ```` ``` #include <Fusion/Fusion/TimelineGroups.h>  // Get the value of the property. boolean propertyValue = timelineGroups_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |