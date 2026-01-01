# ChoiceParameterValue.objectType Property

Parent Object: [ChoiceParameterValue](ChoiceParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ChoiceParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object.  ```` ``` # Get the value of the property. propertyValue = choiceParameterValue_var.objectType ``` ```` |

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object. ```` ``` #include <Cam/Operations/ChoiceParameterValue.h>  // Get the value of the property. string propertyValue = choiceParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |