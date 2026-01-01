# CAMExportOptions.thumbnailPath Property

Parent Object: [CAMExportOptions](CAMExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

Path to the thumbnail for the buildfile

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. |

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. ```` ``` #include <Cam/CAM/CAMExportOptions.h>  // Get the value of the property. string propertyValue = cAMExportOptions_var->thumbnailPath();  // Set the value of the property, where value_var is a string. bool returnValue = cAMExportOptions_var->thumbnailPath(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |