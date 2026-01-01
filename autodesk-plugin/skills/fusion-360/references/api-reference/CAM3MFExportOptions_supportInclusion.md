# CAM3MFExportOptions.supportInclusion Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

Flag setting if support information should be included in the exported file. Includes both support structures marked as open or closed support as well as meta data used in Netfabb. This option might not be available for all machine types. The default value is NotIncluded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. CAM3MFSupportInclusionType propertyValue = cAM3MFExportOptions_var->supportInclusion();  // Set the value of the property, where value_var is a CAM3MFSupportInclusionType. bool returnValue = cAM3MFExportOptions_var->supportInclusion(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CAM3MFSupportInclusionType](CAM3MFSupportInclusionType.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |