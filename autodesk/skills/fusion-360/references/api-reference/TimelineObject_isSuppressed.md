# TimelineObject.isSuppressed Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Gets and sets if this object is suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object. |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. boolean propertyValue = timelineObject_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = timelineObject_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |