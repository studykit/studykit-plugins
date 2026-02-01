# SheetMetalRule.threeBendReliefShape Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

Gets and sets the relief shape to use when three bends intersect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. ThreeBendReliefShapes propertyValue = sheetMetalRule_var->threeBendReliefShape();  // Set the value of the property, where value_var is a ThreeBendReliefShapes. bool returnValue = sheetMetalRule_var->threeBendReliefShape(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThreeBendReliefShapes](ThreeBendReliefShapes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |