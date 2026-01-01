# Scripts.item Method

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Function that returns the specified script or add-in using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object.```` ``` returnValue = scripts_var.item(index) ``` ```` |

"scripts\_var" is a variable referencing a [Scripts](Scripts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Script](Script.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |