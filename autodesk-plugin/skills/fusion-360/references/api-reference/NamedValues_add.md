# NamedValues.add Method

Parent Object: [NamedValues](NamedValues.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

Adds a name value pair to the NamedValues object

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedValues\_var" is a variable referencing a [NamedValues](NamedValues.htm) object.```` ``` returnValue = namedValues_var.add(name, value) ``` ```` |

"namedValues\_var" is a variable referencing a [NamedValues](NamedValues.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the name value pair is added successfully. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | A name for the name value pair |
| value | [ValueInput](ValueInput.htm) | A ValueInput object that defines the value of the name value pair |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |