# PathPatternFeature.timelineObject Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = pathPatternFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |