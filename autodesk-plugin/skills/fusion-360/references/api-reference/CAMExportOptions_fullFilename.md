# CAMExportOptions.fullFilename Property

Parent Object: [CAMExportOptions](CAMExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

The file we want to export to. Needs to contain a valid path, as no intermediate folders are created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. |

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. ```` ``` #include <Cam/CAM/CAMExportOptions.h>  // Get the value of the property. string propertyValue = cAMExportOptions_var->fullFilename();  // Set the value of the property, where value_var is a string. bool returnValue = cAMExportOptions_var->fullFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |