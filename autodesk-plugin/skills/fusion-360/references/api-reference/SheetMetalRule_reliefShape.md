# SheetMetalRule.reliefShape Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

Gets and sets the bend relief shape to use.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. BendReliefShapes propertyValue = sheetMetalRule_var->reliefShape();  // Set the value of the property, where value_var is a BendReliefShapes. bool returnValue = sheetMetalRule_var->reliefShape(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BendReliefShapes](BendReliefShapes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |