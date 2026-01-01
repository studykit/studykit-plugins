# Document.name Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

This property gets and sets the name of the document. You can only set the name of a document before the document is saved for the first time. You can use the isSaved property to determine this. If the document has not been saved and the name is changed, the specified name will be the default name shown in the Save dialog, which the user can modify before saving the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object.  ```` ``` # Get the value of the property. propertyValue = document_var.name  # Set the value of the property. document_var.name = propertyValue ``` ```` |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. string propertyValue = document_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = document_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |