# DrawingExportManager.createPDFExportOptions Method

Parent Object: [DrawingExportManager](DrawingExportManager.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportManager.h>

## Description

Defines the various settings for a STEP export.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportManager\_var" is a variable referencing a [DrawingExportManager](DrawingExportManager.htm) object.```` ``` returnValue = drawingExportManager_var.createPDFExportOptions(filename) ``` ```` |

"drawingExportManager\_var" is a variable referencing a [DrawingExportManager](DrawingExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PDFExportOptions](PDFExportOptions.htm) | Returns a PDFExportOptions object if successful and null if it should fail. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The name of the file to export to. Use settings on the returned PDFExportOptions object to change other settings. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |