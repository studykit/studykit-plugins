# SphereFeature.timelineObject Property

Parent Object: [SphereFeature](SphereFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeature.h>

## Description

Returns the timeline object associated with this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeature\_var" is a variable referencing a SphereFeature object. |

"sphereFeature\_var" is a variable referencing a SphereFeature object. ```` ``` #include <Fusion/Features/SphereFeature.h>  // Get the value of the property. Ptr<TimelineObject> propertyValue = sphereFeature_var->timelineObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TimelineObject](TimelineObject.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |