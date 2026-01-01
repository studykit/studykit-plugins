# BrowserCommandInput.parentCommand Property

Parent Object: [BrowserCommandInput](BrowserCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BrowserCommandInput.h>

## Description

Gets the parent Command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. |

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. ```` ``` #include <Core/UserInterface/BrowserCommandInput.h>  // Get the value of the property. Ptr<Command> propertyValue = browserCommandInput_var->parentCommand(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |