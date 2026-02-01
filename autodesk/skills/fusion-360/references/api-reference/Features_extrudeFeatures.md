# Features.extrudeFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the extrude features within the component and supports the creation of new extrude features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ExtrudeFeatures> propertyValue = features_var->extrudeFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtrudeFeatures](ExtrudeFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extrudeFeatures.addSimple](extrudeFeatures_addSimple_Sample.htm) | Demonstrates the extrudeFeatures.addSimple method. |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setOneSideExtent](extrudeFeaturesOneSideExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setOneSideExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using setSymmetricExtent](extrudeFeaturesSymmetricExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setSymmetricExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using thin extrude](extrudeFeaturesThin_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setThinExtrude method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the thin extrusion. |
| [extrudeFeatures.add using ThroughAllExtent](extrudeFeaturesThroughAllExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the ThroughAllExtent method. |
| [extrudeFeatures.add using setTwoSidesExtent](extrudeFeaturesTwoSidesExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setTwoSidesExtent method. To use this sample have a design open that contains a profile and a body that is positioned away from the profile but is a size where when the profile is extruded it will intersect the body. When you run the script you will be prompted to select the profile that will be used to create the extrusion and the body to extrude to. The extrusion will be created up to the body with an offset and will also be offset from the sketch plane. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |