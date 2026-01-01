# DraftFeature.setTwoAngles Method

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Changes the definition of the feature so that the surfaces are split along the draft plane and the faces on each side of the plane are drafted independently from the other side.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object.```` ``` returnValue = draftFeature_var.setTwoAngles(angleOne, angleTwo) ``` ```` |

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object.  ```` ``` #include <Fusion/Features/DraftFeature.h>  returnValue = draftFeature_var->setTwoAngles(angleOne, angleTwo); ``` ```` |

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