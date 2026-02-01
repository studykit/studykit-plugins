# CAMExportFuture.error Property

Parent Object: [CAMExportFuture](CAMExportFuture.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportFuture.h>

## Description

Gets the last encountered error message generated on the export thread.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object. |

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object. ```` ``` #include <Cam/CAM/CAMExportFuture.h>  // Get the value of the property. string propertyValue = cAMExportFuture_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |