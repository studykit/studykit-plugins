# CAMExportOptions.isValid Property

Parent Object: [CAMExportOptions](CAMExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. |

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. ```` ``` #include <Cam/CAM/CAMExportOptions.h>  // Get the value of the property. boolean propertyValue = cAMExportOptions_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |