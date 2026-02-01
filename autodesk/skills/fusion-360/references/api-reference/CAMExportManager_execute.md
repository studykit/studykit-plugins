# CAMExportManager.execute Method

Parent Object: [CAMExportManager](CAMExportManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportManager.h>

## Description

Executes an export based on the export options.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object.```` ``` returnValue = cAMExportManager_var.execute(exportOptions) ``` ```` |

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the export finished successfully. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| exportOptions | [CAMExportOptions](CAMExportOptions.htm) | The export options defining the export type and necessary meta data. |

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |