# LoftSection.setPointTangentEndCondition Method

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Set the end condition to a tangent condition in the case where the section is a point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.```` ``` returnValue = loftSection_var.setPointTangentEndCondition(weight) ``` ```` |

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.  ```` ``` #include <Fusion/Features/LoftSection.h>  returnValue = loftSection_var->setPointTangentEndCondition(weight); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| weight | [ValueInput](ValueInput.htm) | Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |