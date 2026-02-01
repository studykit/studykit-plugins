# Palette.setMinimumSize Method

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Sets the minimum size of the palette. The user cannot resize it to be smaller than this size. This does not change the current size of the palette unless the palette is already smaller than this size.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a [Palette](Palette.htm) object.```` ``` returnValue = palette_var.setMinimumSize(width, height) ``` ```` |

"palette\_var" is a variable referencing a [Palette](Palette.htm) object.  ```` ``` #include <Core/UserInterface/Palette.h>  returnValue = palette_var->setMinimumSize(width, height); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the minimum size was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | Specifies the minimum width of the palette. |
| height | integer | Specifies the minimum height of the palette. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |