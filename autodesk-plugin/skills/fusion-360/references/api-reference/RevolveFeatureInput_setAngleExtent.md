# RevolveFeatureInput.setAngleExtent Method

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Defines the extent of the revolution to be at a specified angle. An angle and whether the extent is symmetric or only in one direction is specified. If it's not symmetric a positive or negative angle can be used to control the direction. If symmetric, the angle is the angle on one side so the entire angle of the revolution will be twice the specified angle. Use an angle of 360 deg or 2 pi radians to create a full revolve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a [RevolveFeatureInput](RevolveFeatureInput.htm) object.```` ``` returnValue = revolveFeatureInput_var.setAngleExtent(isSymmetric, angle) ``` ```` |

"revolveFeatureInput\_var" is a variable referencing a [RevolveFeatureInput](RevolveFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isSymmetric | boolean | Set to 'true' for a revolve symmetrical about the profile plane |
| angle | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle of the revolution |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [revolveFeatures.add](revolveFeatures_add_Sample.htm) | Demonstrates creating a revolve feature using an angle extent. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |