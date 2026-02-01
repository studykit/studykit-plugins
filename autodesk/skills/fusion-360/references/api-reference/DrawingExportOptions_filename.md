# DrawingExportOptions.filename Property

Parent Object: [DrawingExportOptions](DrawingExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object. |

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object. ```` ``` #include <Drawing/Drawing/DrawingExportOptions.h>  // Get the value of the property. string propertyValue = drawingExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = drawingExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |