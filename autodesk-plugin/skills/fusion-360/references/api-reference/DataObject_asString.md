# DataObject.asString Method

Parent Object: [DataObject](DataObject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObject.h>

## Description

Gets the file as a string (UTF-8). This is convenient when the saved file contains string data. For example, if the file contains JSON data. This eliminates the need to convert the Base64 string into a standard string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object.```` ``` returnValue = dataObject_var.asString() ``` ```` |

"dataObject\_var" is a variable referencing a [DataObject](DataObject.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the data as a standard (UTF-8) string. Fails with an appropriate error in the case where the data cannot be provided. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |