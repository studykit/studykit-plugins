# HoleFeatureInput.setLengthAndOffset Method

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Sets the length and offset of the thread of a tapped hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object.```` ``` returnValue = holeFeatureInput_var.setLengthAndOffset(length, offset) ``` ```` |

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  returnValue = holeFeatureInput_var->setLengthAndOffset(length, offset); ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| length | [ValueInput](ValueInput.htm) | Sets the length of the thread. |
| offset | [ValueInput](ValueInput.htm) | Sets the offset of the thread from the start of the hole. A value of zero is valid for no offset. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |