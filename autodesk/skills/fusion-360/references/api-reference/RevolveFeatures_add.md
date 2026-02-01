# RevolveFeatures.add Method

Parent Object: [RevolveFeatures](RevolveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

Creates a new revolve feature based on the information provided by the provided RevolveFeatureInput object. To create a new revolve, use the createInput function to create a new input object and then use the methods and properties on that object to define the required input for a revolve. Once the information is defined on the input object you can pass it to the Add method to create the revolve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object.```` ``` returnValue = revolveFeatures_var.add(input) ``` ```` |

"revolveFeatures\_var" is a variable referencing a [RevolveFeatures](RevolveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RevolveFeature](RevolveFeature.htm) | Returns the newly created RevolveFeature or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [RevolveFeatureInput](RevolveFeatureInput.htm) | The RevolveFeatureInput object that specifies the input needed to create a new extrude |

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