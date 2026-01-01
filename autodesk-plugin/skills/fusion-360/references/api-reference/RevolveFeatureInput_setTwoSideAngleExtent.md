# RevolveFeatureInput.setTwoSideAngleExtent Method

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Defines the angle of the revolve to be to applied to both sides of the profile at the specified angles.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a [RevolveFeatureInput](RevolveFeatureInput.htm) object.```` ``` returnValue = revolveFeatureInput_var.setTwoSideAngleExtent(angleOne, angleTwo) ``` ```` |

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
| angleOne | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle for the first side of the revolution |
| angleTwo | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle for the second side of the revolution |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |