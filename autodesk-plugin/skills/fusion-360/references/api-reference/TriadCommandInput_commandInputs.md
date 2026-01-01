# TriadCommandInput.commandInputs Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = triadCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |