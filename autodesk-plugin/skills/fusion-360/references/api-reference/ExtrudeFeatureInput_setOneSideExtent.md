# ExtrudeFeatureInput.setOneSideExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Defines the extrusion to go in one direction from the profile. The extent of the extrusion is defined by the extent argument.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Uses no optional arguments. returnValue = extrudeFeatureInput_var->setOneSideExtent(extent, direction);  // Uses optional arguments. returnValue = extrudeFeatureInput_var->setOneSideExtent(extent, direction, taperAngle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the input to a one sided extent was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| extent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| direction | [ExtentDirections](ExtentDirections.htm) | Specifies the direction of the extrusion. PositiveExtentDirection and NegativeExtentDirection are valid values. PositiveExtentDirection is in the same direction as the normal of the profile's parent sketch plane. |
| taperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setOneSideExtent](extrudeFeaturesOneSideExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setOneSideExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using ThroughAllExtent](extrudeFeaturesThroughAllExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the ThroughAllExtent method. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |