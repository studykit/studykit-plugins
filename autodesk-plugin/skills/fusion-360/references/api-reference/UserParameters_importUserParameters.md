# UserParameters.importUserParameters Method

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Function that imports a list of user parameters from a csv file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object.```` ``` returnValue = userParameters_var.importUserParameters(filename) ``` ```` |

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object.  ```` ``` #include <Fusion/Fusion/UserParameters.h>  returnValue = userParameters_var->importUserParameters(filename); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns whether the import was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | string | The full filename (path and file) of the file to read the parameters from. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |