# DrawingDocument.creationId Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

Returns the creation ID of this document. When a new document is created, Fusion assigns it a creation ID that will remain constant for the life of the document. The ID that is assigned is unique. However, it's possible that more than one document can have the same ID. This happens in the case where a document is copied. In this case a new document is created but an existing document is copied. It's only when a new document is created that a creation ID is generated and assigned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object.  ```` ``` # Get the value of the property. propertyValue = drawingDocument_var.creationId ``` ```` |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. string propertyValue = drawingDocument_var->creationId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |