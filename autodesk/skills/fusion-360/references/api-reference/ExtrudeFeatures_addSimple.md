# ExtrudeFeatures.addSimple Method

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Creates a basic extrusion that goes from the profile plane the specified distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object.```` ``` returnValue = extrudeFeatures_var.addSimple(profile, distance, operation) ``` ```` |

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtrudeFeature](ExtrudeFeature.htm) | Returns the newly created ExtrudeFeature or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profile | [Base](Base.htm) | The profile argument can be a single Profile, a single planar face, a single SketchText object, or an ObjectCollection consisting of multiple profiles, planar faces, and sketch texts. When an ObjectCollection is used all of the profiles, faces, and sketch texts must be co-planar.   This method can only be used to create solid extrusions. To create a surface extrusion you need to use the add method. |
| distance | [ValueInput](ValueInput.htm) | ValueInput object that defines the extrude distance. A positive value extrudes in the positive direction of the sketch plane and negative value is in the opposite direction. |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extrudeFeatures.addSimple](extrudeFeatures_addSimple_Sample.htm) | Demonstrates the extrudeFeatures.addSimple method. |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |