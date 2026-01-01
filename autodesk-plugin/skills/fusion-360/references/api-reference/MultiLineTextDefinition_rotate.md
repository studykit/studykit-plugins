# MultiLineTextDefinition.rotate Method

Parent Object: [MultiLineTextDefinition](MultiLineTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

Rotates the text box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiLineTextDefinition\_var" is a variable referencing a [MultiLineTextDefinition](MultiLineTextDefinition.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"multiLineTextDefinition\_var" is a variable referencing a [MultiLineTextDefinition](MultiLineTextDefinition.htm) object.  ```` ``` #include <Fusion/Sketch/MultiLineTextDefinition.h>  // Uses no optional arguments. returnValue = multiLineTextDefinition_var->rotate(angle);  // Uses optional arguments. returnValue = multiLineTextDefinition_var->rotate(angle, keyPoint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angle | double | The angle to rotate the text, specified in radians. |
| keyPoint | [TextBoxKeyPoints](TextBoxKeyPoints.htm) | The key point the rotation is defined around. This is optional and defaults the center of the text box.   This is an optional argument whose default value is TextBoxKeyPoints.MiddleTextBoxKeyPoint. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |