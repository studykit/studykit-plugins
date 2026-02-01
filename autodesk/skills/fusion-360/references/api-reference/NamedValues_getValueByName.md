# NamedValues.getValueByName Method

Parent Object: [NamedValues](NamedValues.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

Function that returns the ValueInput object of a name value pair by specifying its name

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedValues\_var" is a variable referencing a [NamedValues](NamedValues.htm) object. |

```` ```  #include <Core/Application/NamedValues.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the name value pair to return the ValueInput object from |
| value | [ValueInput](ValueInput.htm) | The ValueInput object |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |