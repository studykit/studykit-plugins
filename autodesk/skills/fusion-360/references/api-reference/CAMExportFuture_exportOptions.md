# CAMExportFuture.exportOptions Property

Parent Object: [CAMExportFuture](CAMExportFuture.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportFuture.h>

## Description

Returns the export option used to define the export associated with this future object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object. |

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object. ```` ``` #include <Cam/CAM/CAMExportFuture.h>  // Get the value of the property. Ptr<CAMExportOptions> propertyValue = cAMExportFuture_var->exportOptions(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMExportOptions](CAMExportOptions.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |