# RadioButtonGroupCommandInput.commandInputs Property

Parent Object: [RadioButtonGroupCommandInput](RadioButtonGroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/RadioButtonGroupCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object. |

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object. ```` ``` #include <Core/UserInterface/RadioButtonGroupCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = radioButtonGroupCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |