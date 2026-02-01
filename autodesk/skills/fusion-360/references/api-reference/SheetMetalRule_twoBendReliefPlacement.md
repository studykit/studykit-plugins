# SheetMetalRule.twoBendReliefPlacement Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

Gets and sets the relief placement for a two bend relief shape. When the relief shape is round, both intersection and tangent are valid placements. For square shape, only intersection is valid. For all other shapes, this property will return NoTwoBendReliefPlacement because the placement option is not used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. TwoBendReliefPlacements propertyValue = sheetMetalRule_var->twoBendReliefPlacement();  // Set the value of the property, where value_var is a TwoBendReliefPlacements. bool returnValue = sheetMetalRule_var->twoBendReliefPlacement(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TwoBendReliefPlacements](TwoBendReliefPlacements.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |