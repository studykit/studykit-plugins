# MoveFeature.redefineAsTranslateXYZ Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Redefines the move feature to be described by a translation in X, Y, and Z.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.redefineAsTranslateXYZ(xDistance, yDistance, zDistance, isDesignSpace) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.  ```` ``` #include <Fusion/Features/MoveFeature.h>  returnValue = moveFeature_var->redefineAsTranslateXYZ(xDistance, yDistance, zDistance, isDesignSpace); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the re-definition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xDistance | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset in the X direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used. |
| yDistance | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset in the Y direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used. |
| zDistance | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset in the Z direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used. |
| isDesignSpace | boolean | Defines if the translation is defined with respect to the design or component space. Design space is the same as the root component space. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |