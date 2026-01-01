# SliderCommandInput.getText Method

Parent Object: [SliderCommandInput](SliderCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SliderCommandInput.h>

## Description

Gets the texts of the slider if text has been defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderCommandInput\_var" is a variable referencing a [SliderCommandInput](SliderCommandInput.htm) object.```` ``` returnValue = sliderCommandInput_var.getText(isLeft) ``` ```` |

"sliderCommandInput\_var" is a variable referencing a [SliderCommandInput](SliderCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the left or right text of the slider. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isLeft | boolean | Indicates to get the left or right text. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |