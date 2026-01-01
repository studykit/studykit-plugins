# ExtrudeFeature.bodies Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeature_var.bodies ``` ```` |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = extrudeFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |