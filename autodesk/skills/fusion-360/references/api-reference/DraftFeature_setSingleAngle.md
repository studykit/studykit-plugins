# DraftFeature.setSingleAngle Method

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Changes the definition of the feature so that a single angle is used for all drafts. If the isSymmetric is true then the faces are split along the parting plane and drafted independently using the same angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object.```` ``` returnValue = draftFeature_var.setSingleAngle(isSymmetric, angle) ``` ```` |

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object.  ```` ``` #include <Fusion/Features/DraftFeature.h>  returnValue = draftFeature_var->setSingleAngle(isSymmetric, angle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isSymmetric | boolean | Set to 'true' if the faces are to be split along the plane and drafted symmetrically. This will have the side effect of setting the isSymmetric property to the same value. |
| angle | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle of the draft. This can be a positive or negative value which will affect the direction of the draft along with the isDirectionFlipped property. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |