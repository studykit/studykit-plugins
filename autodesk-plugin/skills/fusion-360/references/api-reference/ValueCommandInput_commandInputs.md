# ValueCommandInput.commandInputs Property

Parent Object: [ValueCommandInput](ValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValueCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. |

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. ```` ``` #include <Core/UserInterface/ValueCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = valueCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |