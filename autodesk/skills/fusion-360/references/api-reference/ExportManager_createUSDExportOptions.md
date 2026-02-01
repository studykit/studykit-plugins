# ExportManager.createUSDExportOptions Method

Parent Object: [ExportManager](ExportManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportManager.h>

## Description

Creates an USDExportOptions object that's used to export a design in USD format. Creation of the USDExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The USDExportOptions supports any available options when exporting to USD format.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"exportManager\_var" is a variable referencing an [ExportManager](ExportManager.htm) object.  ```` ``` #include <Fusion/Fusion/ExportManager.h>  // Uses no optional arguments. returnValue = exportManager_var->createUSDExportOptions(filename);  // Uses optional arguments. returnValue = exportManager_var->createUSDExportOptions(filename, geometry); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [USDExportOptions](USDExportOptions.htm) | The created USDExportOptions object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The filename of the USD file to be created. |
| geometry | [Base](Base.htm) | The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.   This is an optional argument whose default value is null. |

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |