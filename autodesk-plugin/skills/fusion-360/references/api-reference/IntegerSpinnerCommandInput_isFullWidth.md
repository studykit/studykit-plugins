# IntegerSpinnerCommandInput.isFullWidth Property

Parent Object: [IntegerSpinnerCommandInput](IntegerSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSpinnerCommandInput.h>

## Description

Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. |

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSpinnerCommandInput.h>  // Get the value of the property. boolean propertyValue = integerSpinnerCommandInput_var->isFullWidth();  // Set the value of the property, where value_var is a boolean. bool returnValue = integerSpinnerCommandInput_var->isFullWidth(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |