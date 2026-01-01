# IntegerSpinnerCommandInput.parentCommand Property

Parent Object: [IntegerSpinnerCommandInput](IntegerSpinnerCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSpinnerCommandInput.h>

## Description

Gets the parent Command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. |

"integerSpinnerCommandInput\_var" is a variable referencing an IntegerSpinnerCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSpinnerCommandInput.h>  // Get the value of the property. Ptr<Command> propertyValue = integerSpinnerCommandInput_var->parentCommand(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |