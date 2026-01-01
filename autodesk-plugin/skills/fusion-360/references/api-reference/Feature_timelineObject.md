# Feature.timelineObject Property

Parent Object: [Feature](Feature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Feature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"feature\_var" is a variable referencing a Feature object. |

"feature\_var" is a variable referencing a Feature object. ```` ``` #include <Fusion/Features/Feature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = feature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |