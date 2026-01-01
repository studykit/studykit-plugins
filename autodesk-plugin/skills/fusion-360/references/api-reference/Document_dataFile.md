# Document.dataFile Property

Parent Object: [Document](Document.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Gets the DataFile that represents this document in A360.

## Syntax

* [Python](#Python)
* [C++](#C++)

"document\_var" is a variable referencing a Document object. |

"document\_var" is a variable referencing a Document object. ```` ``` #include <Core/Application/Document.h>  // Get the value of the property. Ptr<DataFile> propertyValue = document_var->dataFile(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |