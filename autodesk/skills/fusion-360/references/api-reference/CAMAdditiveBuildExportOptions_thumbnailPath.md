# CAMAdditiveBuildExportOptions.thumbnailPath Property

Parent Object: [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportOptions.h>

## Description

Path to the thumbnail for the buildfile

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. |

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportOptions.h>  // Get the value of the property. string propertyValue = cAMAdditiveBuildExportOptions_var->thumbnailPath();  // Set the value of the property, where value_var is a string. bool returnValue = cAMAdditiveBuildExportOptions_var->thumbnailPath(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |