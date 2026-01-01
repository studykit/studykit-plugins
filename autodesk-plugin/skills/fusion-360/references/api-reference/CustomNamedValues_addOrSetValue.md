# CustomNamedValues.addOrSetValue Method![](../images/TestTubeLarge.png)

Parent Object: [CustomNamedValues](CustomNamedValues.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomNamedValues.h>

## Description

Adds or updates a value. If the specified ID does not exist, a new named value is added. If the ID does exist, the named value is updated with the specified value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customNamedValues\_var" is a variable referencing a [CustomNamedValues](CustomNamedValues.htm) object.```` ``` returnValue = customNamedValues_var.addOrSetValue(id, value) ``` ```` |

"customNamedValues\_var" is a variable referencing a [CustomNamedValues](CustomNamedValues.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is successful and false if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the value to create or change. |
| value | string | The string to assign to the value. |

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |