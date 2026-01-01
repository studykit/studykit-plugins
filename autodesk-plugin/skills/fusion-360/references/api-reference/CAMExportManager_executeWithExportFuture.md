# CAMExportManager.executeWithExportFuture Method

Parent Object: [CAMExportManager](CAMExportManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportManager.h>

## Description

Executes an export based on the export options

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object.```` ``` returnValue = cAMExportManager_var.executeWithExportFuture(exportOptions) ``` ```` |

"cAMExportManager\_var" is a variable referencing a [CAMExportManager](CAMExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMExportFuture](CAMExportFuture.htm) | Returns a CAMExportFuture object if the export has started successfully. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| exportOptions | [CAMExportOptions](CAMExportOptions.htm) | The export options defining the export type and necessary meta data. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |