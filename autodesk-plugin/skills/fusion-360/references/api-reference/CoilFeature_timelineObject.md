# CoilFeature.timelineObject Property

Parent Object: [CoilFeature](CoilFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeature\_var" is a variable referencing a CoilFeature object. |

"coilFeature\_var" is a variable referencing a CoilFeature object. ```` ``` #include <Fusion/Features/CoilFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = coilFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |