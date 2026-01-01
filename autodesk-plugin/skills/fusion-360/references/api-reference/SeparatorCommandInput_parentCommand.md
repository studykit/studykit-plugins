# SeparatorCommandInput.parentCommand Property

Parent Object: [SeparatorCommandInput](SeparatorCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorCommandInput.h>

## Description

Gets the parent Command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. |

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. ```` ``` #include <Core/UserInterface/SeparatorCommandInput.h>  // Get the value of the property. Ptr<Command> propertyValue = separatorCommandInput_var->parentCommand(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |