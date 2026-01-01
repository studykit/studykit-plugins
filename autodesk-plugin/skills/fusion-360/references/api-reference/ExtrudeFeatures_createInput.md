# ExtrudeFeatures.createInput Method

Parent Object: [ExtrudeFeatures](ExtrudeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatures.h>

## Description

Creates a new ExtrudeFeatureInput object that is used to specify the input needed to create a new extrude feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object.```` ``` returnValue = extrudeFeatures_var.createInput(profile, operation) ``` ```` |

"extrudeFeatures\_var" is a variable referencing an [ExtrudeFeatures](ExtrudeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) | Returns the newly created ExtrudeFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profile | [Base](Base.htm) | The profile argument can be a single Profile, a single planar face, a single SketchText object, or an ObjectCollection consisting of multiple profiles, planar faces, and sketch texts. When an ObjectCollection is used all of the profiles, faces, and sketch texts must be co-planar.   To create a surface (non-solid) extrusion, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. You also need to set the isSolid property of the returned ExtrudeFeatureInput property to False. |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setOneSideExtent](extrudeFeaturesOneSideExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setOneSideExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using setSymmetricExtent](extrudeFeaturesSymmetricExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setSymmetricExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using thin extrude](extrudeFeaturesThin_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setThinExtrude method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the thin extrusion. |
| [extrudeFeatures.add using ThroughAllExtent](extrudeFeaturesThroughAllExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the ThroughAllExtent method. |
| [extrudeFeatures.add using setTwoSidesExtent](extrudeFeaturesTwoSidesExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setTwoSidesExtent method. To use this sample have a design open that contains a profile and a body that is positioned away from the profile but is a size where when the profile is extruded it will intersect the body. When you run the script you will be prompted to select the profile that will be used to create the extrusion and the body to extrude to. The extrusion will be created up to the body with an offset and will also be offset from the sketch plane. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |