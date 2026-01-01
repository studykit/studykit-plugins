# CAM3MFExportOptions.isVolumetricDataIncluded Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

Flag toggling if volumetric data should be included in the exported file. The flag is only evaluated if the user has bought the product design extension. The default value is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. boolean propertyValue = cAM3MFExportOptions_var->isVolumetricDataIncluded();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAM3MFExportOptions_var->isVolumetricDataIncluded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |