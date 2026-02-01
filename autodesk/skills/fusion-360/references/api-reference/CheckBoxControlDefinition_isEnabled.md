# CheckBoxControlDefinition.isEnabled Property

Parent Object: [CheckBoxControlDefinition](CheckBoxControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CheckBoxControlDefinition.h>

## Description

Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls.

## Syntax

* [Python](#Python)
* [C++](#C++)

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object. |

"checkBoxControlDefinition\_var" is a variable referencing a CheckBoxControlDefinition object. ```` ``` #include <Core/UserInterface/CheckBoxControlDefinition.h>  // Get the value of the property. boolean propertyValue = checkBoxControlDefinition_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = checkBoxControlDefinition_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |