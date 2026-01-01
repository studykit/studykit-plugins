# Drawing.exportManager Property

Parent Object: [Drawing](Drawing.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/Drawing.h>

## Description

Returns the DrawingExportManager for this drawing. You use the ExportManager to export the drawing in various formats.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawing\_var" is a variable referencing a Drawing object. |

"drawing\_var" is a variable referencing a Drawing object. ```` ``` #include <Drawing/Drawing/Drawing.h>  // Get the value of the property. Ptr<DrawingExportManager> propertyValue = drawing_var->exportManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [DrawingExportManager](DrawingExportManager.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |