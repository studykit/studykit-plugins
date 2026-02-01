# FlatPattern.timelineObject Property

Parent Object: [FlatPattern](FlatPattern.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPattern\_var" is a variable referencing a FlatPattern object. |

"flatPattern\_var" is a variable referencing a FlatPattern object. ```` ``` #include <Fusion/SheetMetal/FlatPattern.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = flatPattern_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |