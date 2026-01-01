# SeparatorCommandInput.parentCommandInput Property

Parent Object: [SeparatorCommandInput](SeparatorCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. |

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. ```` ``` #include <Core/UserInterface/SeparatorCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = separatorCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |