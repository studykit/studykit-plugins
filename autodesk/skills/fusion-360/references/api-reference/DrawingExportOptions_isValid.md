# DrawingExportOptions.isValid Property

Parent Object: [DrawingExportOptions](DrawingExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportOptions.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object. |

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object. ```` ``` #include <Drawing/Drawing/DrawingExportOptions.h>  // Get the value of the property. boolean propertyValue = drawingExportOptions_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |