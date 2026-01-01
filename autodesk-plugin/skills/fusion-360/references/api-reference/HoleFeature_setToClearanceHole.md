# HoleFeature.setToClearanceHole Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setToClearanceHole(clearanceHoleInfo) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting to a clearance hole was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| clearanceHoleInfo | [ClearanceHoleInfo](ClearanceHoleInfo.htm) | The ClearanceHoleInfo object that specifies the size of the clearance hole. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |