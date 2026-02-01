# TSplineBodies.addByTSMDescription Method

Parent Object: [TSplineBodies](TSplineBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

Creates a new TSplineBody using the T-Spline description provided by the input string which contains TSM formatted text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object.```` ``` returnValue = tSplineBodies_var.addByTSMDescription(tsmDescription) ``` ```` |

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TSplineBody](TSplineBody.htm) | Returns the newly created TSplineBody if successful or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tsmDescription | string | A string that contains a T-Spline description in TSM form. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |