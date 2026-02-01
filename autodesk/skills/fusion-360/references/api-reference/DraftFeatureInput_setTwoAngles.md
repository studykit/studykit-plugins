# DraftFeatureInput.setTwoAngles Method

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Defines both angles to use when the surfaces are split along the draft plane and the faces on each side of the plane are drafted independently from the other side.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a [DraftFeatureInput](DraftFeatureInput.htm) object.```` ``` returnValue = draftFeatureInput_var.setTwoAngles(angleOne, angleTwo) ``` ```` |

"draftFeatureInput\_var" is a variable referencing a [DraftFeatureInput](DraftFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angleOne | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle for the faces on the first side of the draft plane. |
| angleTwo | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle for the faces on the second side of the draft plane. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |