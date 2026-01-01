# DataObject.getAsBase64String Method

Parent Object: [DataObject](DataObject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObject.h>

## Description

Gets the binary data represented by the DataObject as a Base64 encoded string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object.```` ``` returnValue = dataObject_var.getAsBase64String() ``` ```` |

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the binary data represented by the DataObject as a standard Base64 encoded string. Fails with an appropriate error in the case where the data cannot be provided. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |