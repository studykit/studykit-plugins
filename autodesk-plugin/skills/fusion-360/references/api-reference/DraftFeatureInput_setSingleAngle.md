# DraftFeatureInput.setSingleAngle Method

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Defines the draft to be defined so that a single angle is used for all drafts. If the isSymmetric is true then the faces are split along the parting plane and drafted independently using the same angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a [DraftFeatureInput](DraftFeatureInput.htm) object.```` ``` returnValue = draftFeatureInput_var.setSingleAngle(isSymmetric, angle) ``` ```` |

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
| isSymmetric | boolean | Set to 'true' if the faces are to be split along the plane and drafted symmetrically. This will have the side effect of setting the isSymmetric property to the same value. |
| angle | [ValueInput](ValueInput.htm) | The ValueInput object that defines the angle of the draft. This can be a positive or negative value which will affect the direction of the draft along with the isDirectionFlipped property. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [draftFeatures.add](draftFeatures_add_Sample.htm) | Demonstrates the draftFeatures.add method. To use this sample, have a design open that contains at least one body. When you run the sample, you will be prompted to select the face to draft. Because the pull direction is using the base X-Y plane, you need to select a face that is not parallel to the X-Y plane. |
| [Draft Feature API Sample](DraftFeatureSample_Sample.htm) | Demonstrates creating a new draft feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |