# Palettes.item Method

Parent Object: [Palettes](Palettes.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palettes.h>

## Description

Returns the specified palette using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palettes\_var" is a variable referencing a [Palettes](Palettes.htm) object.```` ``` returnValue = palettes_var.item(index) ``` ```` |

"palettes\_var" is a variable referencing a [Palettes](Palettes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Palette](Palette.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |