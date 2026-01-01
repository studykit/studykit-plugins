# UserInterface.objectType Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object.  ```` ``` # Get the value of the property. propertyValue = userInterface_var.objectType ``` ```` |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. string propertyValue = userInterface_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |