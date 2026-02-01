# DrawingExportManager.execute Method

Parent Object: [DrawingExportManager](DrawingExportManager.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportManager.h>

## Description

Executes the export operation to create the file in the format specified by the input ExportOptions object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportManager\_var" is a variable referencing a [DrawingExportManager](DrawingExportManager.htm) object.```` ``` returnValue = drawingExportManager_var.execute(exportOptions) ``` ```` |

"drawingExportManager\_var" is a variable referencing a [DrawingExportManager](DrawingExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the export was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| exportOptions | [DrawingExportOptions](DrawingExportOptions.htm) | A DrawingExportOptions object that is created using one of the create methods on the DrawingExportManager object. This defines the type of export and defines the options supported for that file type. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |