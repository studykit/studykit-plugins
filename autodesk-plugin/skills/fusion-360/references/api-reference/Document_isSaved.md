# Document.isSaved Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Property that indicates if this document has been saved or not. The initial save of a document requires that the name and location be specified and requires the saveAs method to be used. If the document has been saved then the save method can be used to save changes made.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object. |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. boolean propertyValue = document_var->isSaved(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |