# TSplineBodies.item Method

Parent Object: [TSplineBodies](TSplineBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

Function that returns the specified T-Spline body using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object.```` ``` returnValue = tSplineBodies_var.item(index) ``` ```` |

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TSplineBody](TSplineBody.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |