# ChoiceProperty.value Property

Parent Object: [ChoiceProperty](ChoiceProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ChoiceProperty.h>

## Description

Gets and sets the which choice is selected from the set of choices. The value is a string that matches one of the predefined choices. The names of the available choices can be obtained using GetChoices method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceProperty\_var" is a variable referencing a ChoiceProperty object. |

"choiceProperty\_var" is a variable referencing a ChoiceProperty object. ```` ``` #include <Core/Application/ChoiceProperty.h>  // Get the value of the property. string propertyValue = choiceProperty_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = choiceProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |