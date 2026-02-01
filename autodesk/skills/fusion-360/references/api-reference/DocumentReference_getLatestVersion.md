# DocumentReference.getLatestVersion Method

Parent Object: [DocumentReference](DocumentReference.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

Updates the reference to use the latest version. This is only useful when the isOutOfDate property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReference\_var" is a variable referencing a [DocumentReference](DocumentReference.htm) object.```` ``` returnValue = documentReference_var.getLatestVersion() ``` ```` |

"documentReference\_var" is a variable referencing a [DocumentReference](DocumentReference.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if getting the latest version was successful. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |