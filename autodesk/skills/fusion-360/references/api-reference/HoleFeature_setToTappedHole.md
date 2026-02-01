# HoleFeature.setToTappedHole Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setToTappedHole(threadInfo) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting to a tapped hole was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadInfo | [ThreadInfo](ThreadInfo.htm) | The ThreadInfo object that specifies the thread to use for the tapped hole. Whether it is straight or tapered tap is defined by the input ThreadInfo object. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |