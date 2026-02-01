# StatusMessage.childStatusMessages Property

Parent Object: [StatusMessage](StatusMessage.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessage.h>

## Description

Returns the collection of status codes that are children of this status message.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessage\_var" is a variable referencing a StatusMessage object. |

"statusMessage\_var" is a variable referencing a StatusMessage object. ```` ``` #include <Core/Application/StatusMessage.h>  // Get the value of the property. Ptr<StatusMessages> propertyValue = statusMessage_var->childStatusMessages(); ``` ```` |

## Property Value

This is a read only property whose value is a [StatusMessages](StatusMessages.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |