# MoveFeature.timelineObject Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object. |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = moveFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |