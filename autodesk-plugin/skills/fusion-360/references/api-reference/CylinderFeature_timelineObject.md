# CylinderFeature.timelineObject Property

Parent Object: [CylinderFeature](CylinderFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. |

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. ```` ``` #include <Fusion/Features/CylinderFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = cylinderFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |