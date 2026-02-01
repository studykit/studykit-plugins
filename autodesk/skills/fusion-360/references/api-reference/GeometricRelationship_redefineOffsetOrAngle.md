# GeometricRelationship.redefineOffsetOrAngle Method![](../images/TestTubeLarge.png)

Parent Object: [GeometricRelationship](GeometricRelationship.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/GeometricRelationship.h>

## Description

This method redefines an existing geometric relationship by defining if it is a mate or angle and specifying a new value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricRelationship\_var" is a variable referencing a [GeometricRelationship](GeometricRelationship.htm) object.```` ``` returnValue = geometricRelationship_var.redefineOffsetOrAngle(isMate, offsetOrAngleValue) ``` ```` |

"geometricRelationship\_var" is a variable referencing a [GeometricRelationship](GeometricRelationship.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isMate | boolean | This argument indicates if the geometric relationship defines a mate or an angle. A value of true indicates a mate relationship. |
| offsetOrAngleValue | [ValueInput](ValueInput.htm) | This argument specifies the value associated with the geometric relationship. If isMate is true, the value is a length, and if it is a real value, then it is centimeters. If it is a string, it is an expression that must evaluate to a length. If isMate is False, the value is an angle, and if it is a real value, then it is radians. If it is a string, it is an expression that must evaluate to an angle. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |