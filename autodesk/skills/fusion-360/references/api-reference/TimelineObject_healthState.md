# TimelineObject.healthState Property

Parent Object: [TimelineObject](TimelineObject.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/TimelineObject.h>

## Description

Returns the current health state of the object associated with this TimelineObject.

## Syntax

* [Python](#Python)
* [C++](#C++)

"timelineObject\_var" is a variable referencing a TimelineObject object. |

"timelineObject\_var" is a variable referencing a TimelineObject object. ```` ``` #include <Fusion/Fusion/TimelineObject.h>  // Get the value of the property. FeatureHealthStates propertyValue = timelineObject_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Ruled Surface Feature API Sample](RuledSurfaceFeatureSample_Sample.htm) | Demonstrates creating a new ruled surface feature. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |