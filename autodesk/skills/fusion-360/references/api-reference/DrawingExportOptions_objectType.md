# DrawingExportOptions.objectType Property

Parent Object: [DrawingExportOptions](DrawingExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object.  ```` ``` # Get the value of the property. propertyValue = drawingExportOptions_var.objectType ``` ```` |

"drawingExportOptions\_var" is a variable referencing a DrawingExportOptions object. ```` ``` #include <Drawing/Drawing/DrawingExportOptions.h>  // Get the value of the property. string propertyValue = drawingExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |