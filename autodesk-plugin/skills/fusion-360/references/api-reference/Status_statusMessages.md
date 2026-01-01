# Status.statusMessages Property

Parent Object: [Status](Status.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Status.h>

## Description

the status messages associated with this status. These messages are displayed to the user in the alert dialog. Each status message can have children status messages that will be displayed as a tree structure in the alert dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"status\_var" is a variable referencing a Status object. |

"status\_var" is a variable referencing a Status object. ```` ``` #include <Core/Application/Status.h>  // Get the value of the property. Ptr<StatusMessages> propertyValue = status_var->statusMessages(); ``` ```` |

## Property Value

This is a read only property whose value is a [StatusMessages](StatusMessages.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |