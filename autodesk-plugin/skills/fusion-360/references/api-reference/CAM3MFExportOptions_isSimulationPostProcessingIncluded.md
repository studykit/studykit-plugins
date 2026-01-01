# CAM3MFExportOptions.isSimulationPostProcessingIncluded Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

Flag toggling if post processing of the simulation should be included. This option might not be available for all machine types. The default value is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. boolean propertyValue = cAM3MFExportOptions_var->isSimulationPostProcessingIncluded();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAM3MFExportOptions_var->isSimulationPostProcessingIncluded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |