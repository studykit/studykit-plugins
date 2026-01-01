# BoolValueCommandInput.parentCommandInput Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = boolValueCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |