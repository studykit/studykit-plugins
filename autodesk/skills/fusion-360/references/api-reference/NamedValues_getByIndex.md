# NamedValues.getByIndex Method

Parent Object: [NamedValues](NamedValues.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

Function that returns the name and ValueInput object of a name value pair by specifying an index number

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
| index | integer | The index of the name value pair to return. The first pair in the collection has an index of 0. |
| name | string | The name |
| value | [ValueInput](ValueInput.htm) | The ValueInput object |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |