# DrawingDocument.allDocumentReferences Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

Returns a collection containing all of the documents referenced directly by this document and those referenced by all sub-assemblies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object. |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. Ptr<DocumentReferences> propertyValue = drawingDocument_var->allDocumentReferences(); ``` ```` |

## Property Value

This is a read only property whose value is a [DocumentReferences](DocumentReferences.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |