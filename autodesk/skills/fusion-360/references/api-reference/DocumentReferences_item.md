# DocumentReferences.item Method

Parent Object: [DocumentReferences](DocumentReferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReferences.h>

## Description

Returns the specified DocumentReference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReferences\_var" is a variable referencing a [DocumentReferences](DocumentReferences.htm) object.```` ``` returnValue = documentReferences_var.item(index) ``` ```` |

"documentReferences\_var" is a variable referencing a [DocumentReferences](DocumentReferences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DocumentReference](DocumentReference.htm) | Returns the specified DocumentReference or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the object to return where the first one in the collection has an index of 0. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |