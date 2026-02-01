# CheckBoxControlDefinition.isChecked Property

Parent Object: [CheckBoxControlDefinition](CheckBoxControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CheckBoxControlDefinition.h>

## Description

Gets or sets whether the check box is checked. Changing this will result in changing any associated controls and will execute the associated command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object. |

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object. ```` ``` #include <Core/UserInterface/CheckBoxControlDefinition.h>  // Get the value of the property. boolean propertyValue = checkBoxControlDefinition_var->isChecked();  // Set the value of the property, where value_var is a boolean. bool returnValue = checkBoxControlDefinition_var->isChecked(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |