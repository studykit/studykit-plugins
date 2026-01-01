# ExportManager.execute Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Executes the export operation to create the file in the format specified by the provided ExportOptions object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` returnValue = exportManager_var.execute(exportOptions) ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the export was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| exportOptions | [ExportOptions](ExportOptions.htm) | An ExportOptions object that is created using one of the create methods on the ExportManager object. This defines the type of file and any available options supported for that file type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ExportManager API Sample](ExportManager_Sample.htm) | Demonstrates how to export f3d to different formats. |
| [Export to other formats API Sample](ExportToOtherFormats_Sample.htm) | Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box. |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |
| [STLExport API Sample](STLExport_Sample.htm) | Demonstrates how to export f3d to STL format. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |