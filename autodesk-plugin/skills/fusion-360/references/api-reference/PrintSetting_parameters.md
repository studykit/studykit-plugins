# PrintSetting.parameters Method

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Function that returns the specified parameterTable using an enum into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object.```` ``` returnValue = printSetting_var.parameters(type) ``` ```` |

"printSetting\_var" is a variable referencing a [PrintSetting](PrintSetting.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMParameters](CAMParameters.htm) | Returns the specified type of parameters or null if an invalid type was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| type | [PrintSettingItemTypes](PrintSettingItemTypes.htm) | The type of the item within the collection to return. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |