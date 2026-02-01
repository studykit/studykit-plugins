# CAMAdditiveBuildExportFilter.isMultiFileExport Property

Parent Object: [CAMAdditiveBuildExportFilter](CAMAdditiveBuildExportFilter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportFilter.h>

## Description

True if the export outputs multiple files. If so, fullFilename should point to a directory, not a file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportFilter\_var" is a variable referencing a CAMAdditiveBuildExportFilter object. |

"cAMAdditiveBuildExportFilter\_var" is a variable referencing a CAMAdditiveBuildExportFilter object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportFilter.h>  // Get the value of the property. boolean propertyValue = cAMAdditiveBuildExportFilter_var->isMultiFileExport(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |