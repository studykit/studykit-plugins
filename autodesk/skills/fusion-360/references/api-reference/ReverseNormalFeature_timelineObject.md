# ReverseNormalFeature.timelineObject Property

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. |

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. ```` ``` #include <Fusion/Features/ReverseNormalFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = reverseNormalFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |