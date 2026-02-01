# ExportOptions.isValid Property

Parent Object: [ExportOptions](ExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportOptions.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportOptions\_var" is a variable referencing an ExportOptions object. |

"exportOptions\_var" is a variable referencing an ExportOptions object. ```` ``` #include <Fusion/Fusion/ExportOptions.h>  // Get the value of the property. boolean propertyValue = exportOptions_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |