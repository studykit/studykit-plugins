# IAddIn.onDeactivate Method

Parent Object: [IAddIn](IAddIn.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IAddIn.h>

## Description

Lets the application do any termination when it is safe to do so. In general, if the add-in is closing, termination should be minimized.

## Syntax

* [Python](#Python)
* [C++](#C++)

"iAddIn\_var" is a variable referencing an [IAddIn](IAddIn.htm) object.```` ``` returnValue = iAddIn_var.onDeactivate(isAppClosing) ``` ```` |

"iAddIn\_var" is a variable referencing an [IAddIn](IAddIn.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isAppClosing | boolean |  |

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |