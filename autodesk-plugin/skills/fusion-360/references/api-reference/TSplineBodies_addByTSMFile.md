# TSplineBodies.addByTSMFile Method

Parent Object: [TSplineBodies](TSplineBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

Creates a new TSplineBody by reading in a TSM file from disk.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBodies\_var" is a variable referencing a [TSplineBodies](TSplineBodies.htm) object.```` ``` returnValue = tSplineBodies_var.addByTSMFile(tsmFilename) ``` ```` |

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
| tsmFilename | string | The full filename of the TSM file on disk. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |