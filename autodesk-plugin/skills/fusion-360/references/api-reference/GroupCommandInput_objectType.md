# GroupCommandInput.objectType Property

Parent Object: [GroupCommandInput](GroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/GroupCommandInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object.  ```` ``` # Get the value of the property. propertyValue = groupCommandInput_var.objectType ``` ```` |

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object. ```` ``` #include <Core/UserInterface/GroupCommandInput.h>  // Get the value of the property. string propertyValue = groupCommandInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |