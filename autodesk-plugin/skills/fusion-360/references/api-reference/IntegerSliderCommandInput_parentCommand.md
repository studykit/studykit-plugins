# IntegerSliderCommandInput.parentCommand Property

Parent Object: [IntegerSliderCommandInput](IntegerSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSliderCommandInput.h>

## Description

Gets the parent Command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. |

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSliderCommandInput.h>  // Get the value of the property. Ptr<Command> propertyValue = integerSliderCommandInput_var->parentCommand(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |