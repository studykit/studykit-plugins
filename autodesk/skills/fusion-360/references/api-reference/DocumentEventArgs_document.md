# DocumentEventArgs.document Property

Parent Object: [DocumentEventArgs](DocumentEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

Provides access to the document that is open. Can be null in the case where the event is fired before the document has been opened or after it has been closed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. |

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. ```` ``` #include <Core/Application/DocumentEventArgs.h>  // Get the value of the property. Ptr<Document> propertyValue = documentEventArgs_var->document(); ``` ```` |

## Property Value

This is a read only property whose value is a [Document](Document.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |