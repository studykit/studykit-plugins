# TextCommandPalette.setMinimumSize Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Sets the minimum size of the palette. The user cannot resize it to be smaller than this size. This does not change the current size of the palette unless the palette is already smaller than this size.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.setMinimumSize(width, height) ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.  ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  returnValue = textCommandPalette_var->setMinimumSize(width, height); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the minimum size was succesful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | Specifies the minimum width of the palette. |
| height | integer | Specifies the minimum height of the palette. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |