# ExportManager.createOBJExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates an OBJExportOptions object that's used to export a design in OBJ format. Creation of the OBJExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.  ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Uses no optional arguments. returnValue = exportManager_var->createOBJExportOptions(geometry);  // Uses optional arguments. returnValue = exportManager_var->createOBJExportOptions(geometry, filename); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OBJExportOptions](OBJExportOptions.htm) | The created createOBJExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometry | [Base](Base.htm) | The geometry to export. This can be a BRepBody, Occurrence, or Component object. |
| filename | string | The filename of the OBJ file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.   This is an optional argument whose default value is "". |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |