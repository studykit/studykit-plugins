# DrawingDocument.objectType Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object.  ```` ``` # Get the value of the property. propertyValue = drawingDocument_var.objectType ``` ```` |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. string propertyValue = drawingDocument_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |