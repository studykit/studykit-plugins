# CAM.checkToolpath Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Checks if the operations (including those nested in sub-folders or patterns) are valid and up to date.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.checkToolpath(operations) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operations are valid |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operations | [Base](Base.htm) | An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |