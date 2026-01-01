# IntegerSliderCommandInput.parentCommandInput Property

Parent Object: [IntegerSliderCommandInput](IntegerSliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/IntegerSliderCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. |

"integerSliderCommandInput\_var" is a variable referencing an IntegerSliderCommandInput object. ```` ``` #include <Core/UserInterface/IntegerSliderCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = integerSliderCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |