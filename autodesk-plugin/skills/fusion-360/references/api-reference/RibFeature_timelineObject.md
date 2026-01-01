# RibFeature.timelineObject Property

Parent Object: [RibFeature](RibFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeature\_var" is a variable referencing a RibFeature object. |

"ribFeature\_var" is a variable referencing a RibFeature object. ```` ``` #include <Fusion/Features/RibFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = ribFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |