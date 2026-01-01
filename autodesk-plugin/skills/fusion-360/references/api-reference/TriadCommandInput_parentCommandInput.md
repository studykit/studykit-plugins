# TriadCommandInput.parentCommandInput Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = triadCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |