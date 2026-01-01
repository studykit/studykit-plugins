# ExportManager.createSTLExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates an STLExportOptions object that's used to export a design in STL format. Creation of the STLExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.  ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Uses no optional arguments. returnValue = exportManager_var->createSTLExportOptions(geometry);  // Uses optional arguments. returnValue = exportManager_var->createSTLExportOptions(geometry, filename); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [STLExportOptions](STLExportOptions.htm) | The created createSTLExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometry | [Base](Base.htm) | The geometry to export. This can be a BRepBody, Occurrence, or Component object. |
| filename | string | The filename of the STL file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.   This is an optional argument whose default value is "". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to other formats API Sample](ExportToOtherFormats_Sample.htm) | Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box. |
| [STLExport API Sample](STLExport_Sample.htm) | Demonstrates how to export f3d to STL format. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |