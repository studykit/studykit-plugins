# CAM3MFExportOptions.areSimulationSurrogatesSplit Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

Flag toggling if surrogate supports used in the simulation should be split. This option might not be available for all machine types. The default value is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. boolean propertyValue = cAM3MFExportOptions_var->areSimulationSurrogatesSplit();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAM3MFExportOptions_var->areSimulationSurrogatesSplit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |