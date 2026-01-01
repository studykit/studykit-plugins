# ChoiceProperty.getChoices Method

Parent Object: [ChoiceProperty](ChoiceProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ChoiceProperty.h>

## Description

Method that returns the list of available choices.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceProperty\_var" is a variable referencing a [ChoiceProperty](ChoiceProperty.htm) object. |

```` ```  #include <Core/Application/ChoiceProperty.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the call was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| names | string[] | An array of the names of the choices. These coincide with the array of choices returned by the choices argument. |
| choices | string[] | An array of the choices. These coincide with the array of names returned by the names argument. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |