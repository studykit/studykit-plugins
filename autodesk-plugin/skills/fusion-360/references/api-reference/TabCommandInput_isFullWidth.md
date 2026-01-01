# TabCommandInput.isFullWidth Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. boolean propertyValue = tabCommandInput_var->isFullWidth();  // Set the value of the property, where value_var is a boolean. bool returnValue = tabCommandInput_var->isFullWidth(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |