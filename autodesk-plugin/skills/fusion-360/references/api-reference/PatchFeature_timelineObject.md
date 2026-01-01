# PatchFeature.timelineObject Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object. |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = patchFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |