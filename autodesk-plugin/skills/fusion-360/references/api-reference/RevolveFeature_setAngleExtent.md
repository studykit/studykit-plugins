# RevolveFeature.setAngleExtent Method

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Defines the extent of the revolution to be at a defined angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.```` ``` returnValue = revolveFeature_var.setAngleExtent(isSymmetric, angle) ``` ```` |

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.  ```` ``` #include <Fusion/Features/RevolveFeature.h>  returnValue = revolveFeature_var->setAngleExtent(isSymmetric, angle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isSymmetric | boolean | Boolean that specifies if the extent is symmetric or not. |
| angle | [ValueInput](ValueInput.htm) | ValueInput object that defines the angle. This can be a string or a value. If it's a string it is interpreted using the current document units and can include equations. For example all of the following are valid as long as they result in angle units; "45", "45 deg", "a1 / 2". If a value is input it is interpreted as radians.   If isSymmetric is false a positive or negative angle can be used to control the direction. If isSymmetric is true, the angle is the extent in one direction so the entire angle of the revolution will be twice the specified angle. Use an angle of 360 deg or 2 pi radians to create a full revolve. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |