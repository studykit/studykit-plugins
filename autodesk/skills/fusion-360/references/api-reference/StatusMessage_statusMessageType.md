# StatusMessage.statusMessageType Property

Parent Object: [StatusMessage](StatusMessage.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessage.h>

## Description

Returns the type of message this StatusMessage represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessage\_var" is a variable referencing a StatusMessage object. |

"statusMessage\_var" is a variable referencing a StatusMessage object. ```` ``` #include <Core/Application/StatusMessage.h>  // Get the value of the property. StatusMessageTypes propertyValue = statusMessage_var->statusMessageType(); ``` ```` |

## Property Value

This is a read only property whose value is a [StatusMessageTypes](StatusMessageTypes.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |