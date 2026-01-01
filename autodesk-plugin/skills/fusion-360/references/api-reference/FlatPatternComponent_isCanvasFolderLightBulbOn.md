# FlatPatternComponent.isCanvasFolderLightBulbOn Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Gets and sets if the light bulb of the canvas folder as seen in the browser is on or off. This controls the visibility of all the canvases in the component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. boolean propertyValue = flatPatternComponent_var->isCanvasFolderLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = flatPatternComponent_var->isCanvasFolderLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |