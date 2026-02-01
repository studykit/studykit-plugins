# CAMExportOptions.exportObject Property

Parent Object: [CAMExportOptions](CAMExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

The export object we want to export. Depending on the actual export option, this might be geometry, an operation or a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. |

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. ```` ``` #include <Cam/CAM/CAMExportOptions.h>  // Get the value of the property. Ptr<Base> propertyValue = cAMExportOptions_var->exportObject();  // Set the value of the property, where value_var is a Base. bool returnValue = cAMExportOptions_var->exportObject(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |