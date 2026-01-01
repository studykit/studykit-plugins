# Document.allDocumentReferences Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Returns a collection containing all of the documents referenced directly by this document and those referenced by all sub-assemblies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object. |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. Ptr<DocumentReferences> propertyValue = document_var->allDocumentReferences(); ``` ```` |

## Property Value

This is a read only property whose value is a [DocumentReferences](DocumentReferences.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |