# UserInterfaceGeneralEvent.objectType Property

Parent Object: [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEvent\_var" is a variable referencing a UserInterfaceGeneralEvent object.  ```` ``` # Get the value of the property. propertyValue = userInterfaceGeneralEvent_var.objectType ``` ```` |

"userInterfaceGeneralEvent\_var" is a variable referencing a UserInterfaceGeneralEvent object. ```` ``` #include <Core/UserInterface/UserInterfaceGeneralEvent.h>  // Get the value of the property. string propertyValue = userInterfaceGeneralEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |