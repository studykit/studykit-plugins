# TSplineBody.saveAsTSMFile Method

Parent Object: [TSplineBody](TSplineBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

Saves the body as a TSM file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBody\_var" is a variable referencing a [TSplineBody](TSplineBody.htm) object.```` ``` returnValue = tSplineBody_var.saveAsTSMFile(filename) ``` ```` |

"tSplineBody\_var" is a variable referencing a [TSplineBody](TSplineBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the file was successfully created. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename of the file to save the body to. If the file already exists, it will be overwritten. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |