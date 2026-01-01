# Documents.item Method

Parent Object: [Documents](Documents.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Documents.h>

## Description

Function that returns the specified document using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documents\_var" is a variable referencing a [Documents](Documents.htm) object.```` ``` returnValue = documents_var.item(index) ``` ```` |

"documents\_var" is a variable referencing a [Documents](Documents.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Document](Document.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |