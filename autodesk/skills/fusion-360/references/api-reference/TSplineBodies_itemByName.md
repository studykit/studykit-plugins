# TSplineBodies.itemByName Method

Parent Object: [TSplineBodies](TSplineBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

Returns a TSplineBody by specifying the name of the body as seen in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object.```` ``` returnValue = tSplineBodies_var.itemByName(name) ``` ```` |

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TSplineBody](TSplineBody.htm) | Returns the specified item or null if a body with that name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the body, as seen in the browser. This is case sensitive. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |