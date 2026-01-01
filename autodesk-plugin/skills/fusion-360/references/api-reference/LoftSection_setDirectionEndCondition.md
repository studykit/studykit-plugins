# LoftSection.setDirectionEndCondition Method

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

Sets the end condition to be defined by a direction and weight.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.```` ``` # Uses no optional arguments. returnValue = loftSection_var.setDirectionEndCondition()  # Uses optional arguments. returnValue = loftSection_var.setDirectionEndCondition(angle, weight) ``` ```` |

"loftSection\_var" is a variable referencing a [LoftSection](LoftSection.htm) object.  ```` ``` #include <Fusion/Features/LoftSection.h>  // Uses no optional arguments. returnValue = loftSection_var->setDirectionEndCondition();  // Uses optional arguments. returnValue = loftSection_var->setDirectionEndCondition(angle, weight); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angle | [ValueInput](ValueInput.htm) | Input ValueInput object that specifies the direction by using an angle. This defaults to an angle of 0.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as an angle. If the ValueInput is a value then it is in radians.   This is an optional argument whose default value is null. |
| weight | [ValueInput](ValueInput.htm) | Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |