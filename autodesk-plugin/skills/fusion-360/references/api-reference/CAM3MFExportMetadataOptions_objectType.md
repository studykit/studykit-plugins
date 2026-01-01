# CAM3MFExportMetadataOptions.objectType Property

Parent Object: [CAM3MFExportMetadataOptions](CAM3MFExportMetadataOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportMetadataOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportMetadataOptions\_var" is a variable referencing a CAM3MFExportMetadataOptions object.  ```` ``` # Get the value of the property. propertyValue = cAM3MFExportMetadataOptions_var.objectType ``` ```` |

"cAM3MFExportMetadataOptions\_var" is a variable referencing a CAM3MFExportMetadataOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportMetadataOptions.h>  // Get the value of the property. string propertyValue = cAM3MFExportMetadataOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |