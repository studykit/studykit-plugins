# Scripts.itemsByName Method

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Function that returns an array of scripts that have the specified name. In most cases this will return an array containing a single script, but it's possible to have more than one script with the same name in the case where the scripts are in different folders.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object.```` ``` returnValue = scripts_var.itemsByName(name) ``` ```` |

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Script](Script.htm)[] | Returns the scripts with the specified name or an empty array if there aren't any scripts with that name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The script name to search for. |

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |