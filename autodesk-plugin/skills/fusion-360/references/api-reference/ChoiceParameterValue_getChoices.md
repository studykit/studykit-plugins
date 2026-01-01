# ChoiceParameterValue.getChoices Method

Parent Object: [ChoiceParameterValue](ChoiceParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ChoiceParameterValue.h>

## Description

Method that returns the list of available choices.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceParameterValue\_var" is a variable referencing a [ChoiceParameterValue](ChoiceParameterValue.htm) object. |

```` ```  #include <Cam/Operations/ChoiceParameterValue.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the call was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| names | string[] | An array of the names of the choices. These coincide with the array of possible values returned by the values argument. |
| values | string[] | An array of the possible values. These coincide with the array of names returned by the names argument. |

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |