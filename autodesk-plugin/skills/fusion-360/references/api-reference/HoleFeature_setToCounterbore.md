# HoleFeature.setToCounterbore Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Calling this method will change the hole to a counterbore hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setToCounterbore(counterboreDiameter, counterboreDepth) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  returnValue = holeFeature_var->setToCounterbore(counterboreDiameter, counterboreDepth); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if changing the hole was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| counterboreDiameter | [ValueInput](ValueInput.htm) | A ValueInput object that defines the counterbore diameter. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length. |
| counterboreDepth | [ValueInput](ValueInput.htm) | A ValueInput object that defines the counterbore depth. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |