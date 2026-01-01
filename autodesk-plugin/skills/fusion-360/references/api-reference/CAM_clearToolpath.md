# CAM.clearToolpath Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Clears all the toolpaths for the specified objects, including those nested in sub-folders or patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.clearToolpath(operations) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Return true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operations | [Base](Base.htm) | An Operation, Setup, Folder, or Pattern object. You can also use and ObjectCollection to specify multiple objects of any combination of types. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |