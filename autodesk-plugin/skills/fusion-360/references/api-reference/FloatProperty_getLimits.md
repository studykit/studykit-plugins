# FloatProperty.getLimits Method

Parent Object: [FloatProperty](FloatProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

Method that returns any limits for the value of this property. The HasLimits property can be used to see if there are any limits or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatProperty\_var" is a variable referencing a [FloatProperty](FloatProperty.htm) object.  ```` ``` (returnValue, hasLowLimit, lowLimit, hasHighLimit, highLimit) = floatProperty_var.getLimits() ``` ```` |

```` ```  #include <Core/Application/FloatProperty.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the method call was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| hasLowLimit | boolean | Output Boolean that indicates if there is a low limit or not. |
| lowLimit | double | If the hasLowLimit argument is true, this argument returns the low limit. |
| hasHighLimit | boolean | Output Boolean that indicates if there is a high limit or not. |
| highLimit | double | If the hasHighLimit argument is true, this argument returns the high limit. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |