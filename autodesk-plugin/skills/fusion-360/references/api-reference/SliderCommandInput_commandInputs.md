# SliderCommandInput.commandInputs Property

Parent Object: [SliderCommandInput](SliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SliderCommandInput.h>

## Description

Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. |

"sliderCommandInput\_var" is a variable referencing a SliderCommandInput object. ```` ``` #include <Core/UserInterface/SliderCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = sliderCommandInput_var->commandInputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |