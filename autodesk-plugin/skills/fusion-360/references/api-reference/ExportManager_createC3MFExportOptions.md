# ExportManager.createC3MFExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates a C3MFExportOptions object that's used to export a design in 3MF format. Creation of the C3MFExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.  ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Uses no optional arguments. returnValue = exportManager_var->createC3MFExportOptions(geometry);  // Uses optional arguments. returnValue = exportManager_var->createC3MFExportOptions(geometry, filename); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [C3MFExportOptions](C3MFExportOptions.htm) | The created createC3MFExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometry | [Base](Base.htm) | The geometry to export. This can be a BRepBody, Occurrence, or Component object. |
| filename | string | The filename of the 3MF file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.   This is an optional argument whose default value is "". |

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |