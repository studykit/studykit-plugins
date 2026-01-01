# TextCommandPalette.snapTo Method

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Snaps this palette to another palette.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object.```` ``` returnValue = textCommandPalette_var.snapTo(palette, snapOption) ``` ```` |

"textCommandPalette\_var" is a variable referencing a [TextCommandPalette](TextCommandPalette.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the palette was successfully snapped to the other palette. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| palette | [Palette](Palette.htm) | Specifies the palette to snap to. |
| snapOption | [PaletteSnapOptions](PaletteSnapOptions.htm) | Specifies how this palette should be snapped to the other palette. |

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |