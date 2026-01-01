# ExportManager.createSMTExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates an SMTExportOptions object that's used to export a design in SMT format. Creation of the SMTExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The SMTExportOptions supports any available options when exporting to SMT format.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.  ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Uses no optional arguments. returnValue = exportManager_var->createSMTExportOptions(filename);  // Uses optional arguments. returnValue = exportManager_var->createSMTExportOptions(filename, geometry); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SMTExportOptions](SMTExportOptions.htm) | The created SMTExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename of the SMT file to be created. |
| geometry | [Base](Base.htm) | The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ExportManager API Sample](ExportManager_Sample.htm) | Demonstrates how to export f3d to different formats. |
| [Export to other formats API Sample](ExportToOtherFormats_Sample.htm) | Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |