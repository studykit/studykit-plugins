# DrawingDocument.name Property

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

This property gets and sets the name of the document. You can only set the name of a document before the document is saved for the first time. You can use the isSaved property to determine this. If the document has not been saved and the name is changed, the specified name will be the default name shown in the Save dialog, which the user can modify before saving the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a DrawingDocument object.  ```` ``` # Get the value of the property. propertyValue = drawingDocument_var.name  # Set the value of the property. drawingDocument_var.name = propertyValue ``` ```` |

"drawingDocument\_var" is a variable referencing a DrawingDocument object. ```` ``` #include <Drawing/Drawing/DrawingDocument.h>  // Get the value of the property. string propertyValue = drawingDocument_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = drawingDocument_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |