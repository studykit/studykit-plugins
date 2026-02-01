# HoleFeature.setDistanceExtent Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Defines the depth of the hole using a specific distance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setDistanceExtent(distance) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  returnValue = holeFeature_var->setDistanceExtent(distance); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the extent was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| distance | [ValueInput](ValueInput.htm) | The depth of the hole. If a real is specified the value is in centimeters. If a string is specified the units are derived from the string. If no units are specified, the default units of the document are used. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |