# DocumentReference.referencedDocument Property

Parent Object: [DocumentReference](DocumentReference.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

The document currently open in Fusion that this object references.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReference\_var" is a variable referencing a DocumentReference object. |

"documentReference\_var" is a variable referencing a DocumentReference object. ```` ``` #include <Core/Application/DocumentReference.h>  // Get the value of the property. Ptr<Document> propertyValue = documentReference_var->referencedDocument(); ``` ```` |

## Property Value

This is a read only property whose value is a [Document](Document.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |