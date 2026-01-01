# DrawingDocument.products Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

Returns the products associated with this document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object. |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. Ptr<Products> propertyValue = drawingDocument_var->products(); ``` ```` |

## Property Value

This is a read only property whose value is a [Products](Products.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |