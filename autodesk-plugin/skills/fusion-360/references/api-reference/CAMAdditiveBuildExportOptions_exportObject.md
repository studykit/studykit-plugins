# CAMAdditiveBuildExportOptions.exportObject Property

Parent Object: [CAMAdditiveBuildExportOptions](CAMAdditiveBuildExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportOptions.h>

## Description

The export object we want to export. Depending on the actual export option, this might be geometry, an operation or a setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. |

"cAMAdditiveBuildExportOptions\_var" is a variable referencing a CAMAdditiveBuildExportOptions object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportOptions.h>  // Get the value of the property. Ptr<Base> propertyValue = cAMAdditiveBuildExportOptions_var->exportObject();  // Set the value of the property, where value_var is a Base. bool returnValue = cAMAdditiveBuildExportOptions_var->exportObject(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |