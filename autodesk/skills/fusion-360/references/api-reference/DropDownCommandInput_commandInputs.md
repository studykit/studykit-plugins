# DropDownCommandInput.commandInputs Property

Parent Object: [DropDownCommandInput](DropDownCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. |

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. ```` ``` #include <Core/UserInterface/DropDownCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = dropDownCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |