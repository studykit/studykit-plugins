# Document.parent Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Returns the parent Application object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object. |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. Ptr<Application> propertyValue = document_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Application](Application.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |