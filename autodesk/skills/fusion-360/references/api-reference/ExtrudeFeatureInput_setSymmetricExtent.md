# ExtrudeFeatureInput.setSymmetricExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Defines the extrusion to go symmetrically in both directions from the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Uses no optional arguments. returnValue = extrudeFeatureInput_var->setSymmetricExtent(distance, isFullLength);  // Uses optional arguments. returnValue = extrudeFeatureInput_var->setSymmetricExtent(distance, isFullLength, taperAngle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the extent was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| distance | [ValueInput](ValueInput.htm) | The distance of the extrusions. This is either the full length of half of the length of the final extrusion depending on the value of the isFullLength property. |
| isFullLength | boolean | Defines if the value defines the full length of the extrusion or half of the length. A value of true indicates it defines the full length. |
| taperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle. The same taper angle is used for both sides for a symmetric extrusion. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [extrudeFeatures.add using setSymmetricExtent](extrudeFeaturesSymmetricExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setSymmetricExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |
| [extrudeFeatures.add using thin extrude](extrudeFeaturesThin_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setThinExtrude method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the thin extrusion. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |