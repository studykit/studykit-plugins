# ExportManager.createDXFSketchExportOptions Method![](../images/TestTubeLarge.png)

Parent Object: [ExportManager](ExportManager.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates a DXFSketchExportOptions object that's used to export a sketch in DXF format. Creation of the DXFSketchExportOptions object does not perform the export. You must call the execute method after changing the settings to the desired values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` returnValue = exportManager_var.createDXFSketchExportOptions(filename, sketch) ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DXFSketchExportOptions](DXFSketchExportOptions.htm) | The created DXFSketchExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename of the DXF file to be created. |
| sketch | [Sketch](Sketch.htm) | The Sketch object to export. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |