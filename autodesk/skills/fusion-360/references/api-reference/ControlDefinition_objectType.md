# ControlDefinition.objectType Property

Parent Object: [ControlDefinition](ControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ControlDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controlDefinition\_var" is a variable referencing a ControlDefinition object.  ```` ``` # Get the value of the property. propertyValue = controlDefinition_var.objectType ``` ```` |

"controlDefinition\_var" is a variable referencing a ControlDefinition object. ```` ``` #include <Core/UserInterface/ControlDefinition.h>  // Get the value of the property. string propertyValue = controlDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |