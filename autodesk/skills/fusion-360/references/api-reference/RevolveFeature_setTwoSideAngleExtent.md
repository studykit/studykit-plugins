# RevolveFeature.setTwoSideAngleExtent Method

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Changes the extent of the revolve to be defined as a two sided angle extent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.```` ``` returnValue = revolveFeature_var.setTwoSideAngleExtent(angleOne, angleTwo) ``` ```` |

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.  ```` ``` #include <Fusion/Features/RevolveFeature.h>  returnValue = revolveFeature_var->setTwoSideAngleExtent(angleOne, angleTwo); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angleOne | [ValueInput](ValueInput.htm) | ValueInput object that defines the first angle. This can be a string or a value. If it's a string it is interpreted using the current document units and can include equations. For example all of the following are valid as long as they result in angle units; "45", "45 deg", "a1 / 2". If a value is input it is interpreted as radians. |
| angleTwo | [ValueInput](ValueInput.htm) | ValueInput object that defines the second angle. This can be a string or a value. If it's a string it is interpreted using the current document units and can include equations. For example all of the following are valid as long as they result in angle units; "45", "45 deg", "a1 / 2". If a value is input it is interpreted as radians. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |