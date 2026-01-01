# ExtrudeFeatureInput.setTwoSidesExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Defines the extrusion to go in both directions from the profile. The extent is defined independently for each direction using the input arguments.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Uses no optional arguments. returnValue = extrudeFeatureInput_var->setTwoSidesExtent(sideOneExtent, sideTwoExtent);  // Uses optional arguments. returnValue = extrudeFeatureInput_var->setTwoSidesExtent(sideOneExtent, sideTwoExtent, sideOneTaperAngle, sideTwoTaperAngle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the extent was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sideOneExtent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion towards side one is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| sideTwoExtent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion towards side two is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| sideOneTaperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle for side one. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |
| sideTwoTaperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle for side two. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setTwoSidesExtent](extrudeFeaturesTwoSidesExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setTwoSidesExtent method. To use this sample have a design open that contains a profile and a body that is positioned away from the profile but is a size where when the profile is extruded it will intersect the body. When you run the script you will be prompted to select the profile that will be used to create the extrusion and the body to extrude to. The extrusion will be created up to the body with an offset and will also be offset from the sketch plane. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |