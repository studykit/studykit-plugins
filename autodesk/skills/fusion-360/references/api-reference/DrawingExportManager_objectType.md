# DrawingExportManager.objectType Property

Parent Object: [DrawingExportManager](DrawingExportManager.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingExportManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingExportManager\_var" is a variable referencing a DrawingExportManager object.  ```` ``` # Get the value of the property. propertyValue = drawingExportManager_var.objectType ``` ```` |

"drawingExportManager\_var" is a variable referencing a DrawingExportManager object. ```` ``` #include <Drawing/Drawing/DrawingExportManager.h>  // Get the value of the property. string propertyValue = drawingExportManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |