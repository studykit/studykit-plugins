# BaseFeature.timelineObject Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object. |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = baseFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |