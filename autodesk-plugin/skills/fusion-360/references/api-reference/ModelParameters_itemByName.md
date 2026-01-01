# ModelParameters.itemByName Method

Parent Object: [ModelParameters](ModelParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameters.h>

## Description

Function that returns the specified Model Parameter using the name of the parameter as it is displayed in the parameters dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameters\_var" is a variable referencing a [ModelParameters](ModelParameters.htm) object.```` ``` returnValue = modelParameters_var.itemByName(name) ``` ```` |

"modelParameters\_var" is a variable referencing a [ModelParameters](ModelParameters.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ModelParameter](ModelParameter.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the Model Parameter as it is displayed in the parameters dialog |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |