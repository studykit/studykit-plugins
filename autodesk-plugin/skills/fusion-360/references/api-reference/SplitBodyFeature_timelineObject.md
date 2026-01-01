# SplitBodyFeature.timelineObject Property

Parent Object: [SplitBodyFeature](SplitBodyFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object. |

"splitBodyFeature\_var" is a variable referencing a SplitBodyFeature object. ```` ``` #include <Fusion/Features/SplitBodyFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = splitBodyFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |