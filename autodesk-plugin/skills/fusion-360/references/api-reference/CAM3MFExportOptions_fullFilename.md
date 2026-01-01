# CAM3MFExportOptions.fullFilename Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

The file we want to export to. Needs to contain a valid path, as no intermediate folders are created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. string propertyValue = cAM3MFExportOptions_var->fullFilename();  // Set the value of the property, where value_var is a string. bool returnValue = cAM3MFExportOptions_var->fullFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |