# CoilFeatureInput.setToRevolutionsAndPitch Method

Parent Object: [CoilFeatureInput](CoilFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatureInput.h>

## Description

Sets the coil type to RevolutionsAndPitchCoilType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatureInput\_var" is a variable referencing a [CoilFeatureInput](CoilFeatureInput.htm) object.```` ``` returnValue = coilFeatureInput_var.setToRevolutionsAndPitch(revolutions, pitch, angle) ``` ```` |

"coilFeatureInput\_var" is a variable referencing a [CoilFeatureInput](CoilFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| revolutions | [ValueInput](ValueInput.htm) | A ValueInput object that defines the number of revolutions. |
| pitch | [ValueInput](ValueInput.htm) | A ValueInput object that defines the pitch. |
| angle | [ValueInput](ValueInput.htm) | A ValueInput object that defines angle. |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |