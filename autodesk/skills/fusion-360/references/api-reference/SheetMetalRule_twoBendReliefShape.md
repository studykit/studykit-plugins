# SheetMetalRule.twoBendReliefShape Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

Gets and sets the relief shape to use when two bends intersect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object.  ```` ``` # Get the value of the property. propertyValue = sheetMetalRule_var.twoBendReliefShape  # Set the value of the property. sheetMetalRule_var.twoBendReliefShape = propertyValue ``` ```` |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. TwoBendReliefShapes propertyValue = sheetMetalRule_var->twoBendReliefShape();  // Set the value of the property, where value_var is a TwoBendReliefShapes. bool returnValue = sheetMetalRule_var->twoBendReliefShape(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TwoBendReliefShapes](TwoBendReliefShapes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |