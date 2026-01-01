# ChoiceProperty.objectType Property

Parent Object: [ChoiceProperty](ChoiceProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ChoiceProperty.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceProperty\_var" is a variable referencing a ChoiceProperty object.  ```` ``` # Get the value of the property. propertyValue = choiceProperty_var.objectType ``` ```` |

"choiceProperty\_var" is a variable referencing a ChoiceProperty object. ```` ``` #include <Core/Application/ChoiceProperty.h>  // Get the value of the property. string propertyValue = choiceProperty_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |