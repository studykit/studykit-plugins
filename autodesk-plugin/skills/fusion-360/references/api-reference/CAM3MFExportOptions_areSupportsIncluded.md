# CAM3MFExportOptions.areSupportsIncluded Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use supportInclusion for setting how to include support.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object.  ```` ``` # Get the value of the property. propertyValue = cAM3MFExportOptions_var.areSupportsIncluded  # Set the value of the property. cAM3MFExportOptions_var.areSupportsIncluded = propertyValue ``` ```` |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. boolean propertyValue = cAM3MFExportOptions_var->areSupportsIncluded();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAM3MFExportOptions_var->areSupportsIncluded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2021
Retired in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |