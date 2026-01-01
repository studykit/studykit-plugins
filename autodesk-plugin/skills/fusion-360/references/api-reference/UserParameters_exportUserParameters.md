# UserParameters.exportUserParameters Method

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Function that exports a list of user parameters to a csv file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object.```` ``` returnValue = userParameters_var.exportUserParameters(userParameterArray, filename) ``` ```` |

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns whether the export was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| userParameterArray | UserParameter[] | The array of user parameters to export. |
| filename | string | The full filename (path and file) of the file to write the parameters to. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |