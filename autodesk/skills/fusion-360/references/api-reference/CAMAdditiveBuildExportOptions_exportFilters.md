# CAMAdditiveBuildExportOptions.exportFilters Property

Parent Object: [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportOptions.h>

## Description

Gets a list of available export filters from the setup's print setting. The export object must be set before using this function.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. |

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportOptions.h>  // Get the value of the property. std::vector<Ptr<CAMAdditiveBuildExportFilter>> propertyValue = cAMAdditiveBuildExportOptions_var->exportFilters(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [CAMAdditiveBuildExportFilter](CAMAdditiveBuildExportFilter.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |