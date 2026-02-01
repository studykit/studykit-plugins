# CAM3MFExportOptions.volumetricDataResolution Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

Integer value representing the resolution of the volumetric data. The value is only evaluated if the user has bought the product design extension. The default value is 128.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. integer propertyValue = cAM3MFExportOptions_var->volumetricDataResolution();  // Set the value of the property, where value_var is an integer. bool returnValue = cAM3MFExportOptions_var->volumetricDataResolution(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |