# CheckBoxControlDefinition.objectType Property

Parent Object: [CheckBoxControlDefinition](CheckBoxControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CheckBoxControlDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object.  ```` ``` # Get the value of the property. propertyValue = checkBoxControlDefinition_var.objectType ``` ```` |

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object. ```` ``` #include <Core/UserInterface/CheckBoxControlDefinition.h>  // Get the value of the property. string propertyValue = checkBoxControlDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |