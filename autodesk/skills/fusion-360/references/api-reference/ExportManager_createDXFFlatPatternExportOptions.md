# ExportManager.createDXFFlatPatternExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates a DXFFlatPatternExport object that's used to export a flat pattern in DXF format. Creation of the DXFFlatPatternExport object does not perform the export. You must call the execute method. You can change any additional settings by setting properties on the returned object before calling the execute method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` returnValue = exportManager_var.createDXFFlatPatternExportOptions(filename, flatPattern) ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DXFFlatPatternExportOptions](DXFFlatPatternExportOptions.htm) | The created DXFFlatPatternExport object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename of the DXF file to be created. |
| flatPattern | [FlatPattern](FlatPattern.htm) | The FlatPattern object to export. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |