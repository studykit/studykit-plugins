# CAMAdditiveBuildExportOptions.error Property

Parent Object: [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportOptions.h>

## Description

Gets the last encountered error message. When the CAMExportManager's executeWithExportFuture() method is used, this method only returns errors encoutered when setting up the export. Errors thrown afterwards can be retrieved via the CAMExportFuture object. When the CAMExportManager's execute() method is used, any error can be retrieved using this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. |

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportOptions.h>  // Get the value of the property. string propertyValue = cAMAdditiveBuildExportOptions_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |