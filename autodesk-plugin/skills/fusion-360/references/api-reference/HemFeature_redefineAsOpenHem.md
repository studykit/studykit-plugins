# HemFeature.redefineAsOpenHem Method![](../images/TestTubeLarge.png)

Parent Object: [HemFeature](HemFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/HemFeature.h>

## Description

Redefines the hem as an open hem.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hemFeature\_var" is a variable referencing a [HemFeature](HemFeature.htm) object.```` ``` returnValue = hemFeature_var.redefineAsOpenHem(length, gap, isFlipped, bendPositionType) ``` ```` |

"hemFeature\_var" is a variable referencing a [HemFeature](HemFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if defining the hem is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| length | [ValueInput](ValueInput.htm) | The length of the hem. |
| gap | [ValueInput](ValueInput.htm) | The gap distance of the hem. |
| isFlipped | boolean | Indicates if the hem direction is flipped. |
| bendPositionType | [BendPositionTypes](BendPositionTypes.htm) | The bend location type for the hem. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |