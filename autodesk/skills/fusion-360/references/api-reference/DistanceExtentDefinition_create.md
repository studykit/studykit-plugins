# DistanceExtentDefinition.create Method

Parent Object: [DistanceExtentDefinition](DistanceExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceExtentDefinition.h>

## Description

Statically creates a new DistanceExtentDefinition object. This is used as input when defining the extents of a feature to be a specified distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DistanceExtentDefinition](DistanceExtentDefinition.htm) | Returns the newly created DistanceExtentDefinition or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| distance | [ValueInput](ValueInput.htm) | A ValueInput that defines the distance of the extrusion. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setOneSideExtent](extrudeFeaturesOneSideExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setOneSideExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using setTwoSidesExtent](extrudeFeaturesTwoSidesExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setTwoSidesExtent method. To use this sample have a design open that contains a profile and a body that is positioned away from the profile but is a size where when the profile is extruded it will intersect the body. When you run the script you will be prompted to select the profile that will be used to create the extrusion and the body to extrude to. The extrusion will be created up to the body with an offset and will also be offset from the sketch plane. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |