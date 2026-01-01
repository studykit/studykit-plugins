# DrawingDocument.isModified Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

Property that indicates if the document has been modified since it was last saved.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object. |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. boolean propertyValue = drawingDocument_var->isModified(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |