# CommandDefinitions.item Method

Parent Object: [CommandDefinitions](CommandDefinitions.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinitions.h>

## Description

Returns the CommandDefinition at the specified index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinitions\_var" is a variable referencing a [CommandDefinitions](CommandDefinitions.htm) object.```` ``` returnValue = commandDefinitions_var.item(index) ``` ```` |

"commandDefinitions\_var" is a variable referencing a [CommandDefinitions](CommandDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CommandDefinition](CommandDefinition.htm) | Returns the CommandDefinition at the specified index or null if an invalid index is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the command definition within the collection to return. The first item in the collection has in index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |