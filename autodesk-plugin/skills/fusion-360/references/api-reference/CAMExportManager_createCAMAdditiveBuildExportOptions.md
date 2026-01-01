# CAMExportManager.createCAMAdditiveBuildExportOptions Method

Parent Object: [CAMExportManager](CAMExportManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportManager.h>

## Description

Creates a new export option based on the print setting's export formats. FFF and DED machines are not supported, their export files are generated using posts.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object.```` ``` returnValue = cAMExportManager_var.createCAMAdditiveBuildExportOptions() ``` ```` |

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm) | Returns new CAMAdditiveBuildExportOptions. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |