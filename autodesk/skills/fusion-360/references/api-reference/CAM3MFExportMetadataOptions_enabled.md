# CAM3MFExportMetadataOptions.enabled Property

Parent Object: [CAM3MFExportMetadataOptions](CAM3MFExportMetadataOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportMetadataOptions.h>

## Description

Enable or disable the integration of Metadata in the 3mf. This is true by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportMetadataOptions\_var" is a variable referencing a CAM3MFExportMetadataOptions object. |

"cAM3MFExportMetadataOptions\_var" is a variable referencing a CAM3MFExportMetadataOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportMetadataOptions.h>  // Get the value of the property. boolean propertyValue = cAM3MFExportMetadataOptions_var->enabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = cAM3MFExportMetadataOptions_var->enabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |