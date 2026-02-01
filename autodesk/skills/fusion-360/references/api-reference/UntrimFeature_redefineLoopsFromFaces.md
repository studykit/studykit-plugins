# UntrimFeature.redefineLoopsFromFaces Method

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Set the loops to be removed from a set of faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a [UntrimFeature](UntrimFeature.htm) object.```` ``` returnValue = untrimFeature_var.redefineLoopsFromFaces(faces, untrimLoopType) ``` ```` |

"untrimFeature\_var" is a variable referencing a [UntrimFeature](UntrimFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns whether the operation was successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| faces | BRepFace[] | An array of BRepFace objects that will have the loops of the specified types removed. Only loops that do not have a connected face can be removed (the edges in the loop have a single face). The array can only contain faces from surface bodies, (the isSolid property of the BRepBody returns false). |
| untrimLoopType | [UntrimLoopTypes](UntrimLoopTypes.htm) | The loop type to be untrimmed (AllLoopUntrimType, InternalLoopUntrimType, or ExternalLoopUntrimType). |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |