# RevolveFeatures.createInput Method

Parent Object: [RevolveFeatures](RevolveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

Creates a new RevolveFeatureInput object that is used to specify the input needed to create a new revolve feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object.```` ``` returnValue = revolveFeatures_var.createInput(profile, axis, operation) ``` ```` |

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RevolveFeatureInput](RevolveFeatureInput.htm) | Returns the newly created RevolveFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profile | [Base](Base.htm) | The profile argument can be a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.   To create a surface (non-solid) revolution, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. You also need to set the isSolid property of the returned RevolveFeatureInput property to False. |
| axis | [Base](Base.htm) | The axis can be a sketch line, construction axis, linear edge or a face that defines an axis (cylinder, cone, torus, etc.). If it is not in the same plane as the profile, it is projected onto the profile plane. |
| operation | [FeatureOperations](FeatureOperations.htm) | The operation type to perform. |

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