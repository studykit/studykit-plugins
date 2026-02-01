# Design.exportManager Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the ExportManager for this design. You use the ExportManager to export the current design in various formats.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<ExportManager> propertyValue = design_var->exportManager(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExportManager](ExportManager.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to other formats API Sample](ExportToOtherFormats_Sample.htm) | Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box. |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |