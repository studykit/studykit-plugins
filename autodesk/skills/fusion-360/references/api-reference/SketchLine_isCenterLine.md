# SketchLine.isCenterLine Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

Gets and sets whether this line is defined as a centerline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object. |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. boolean propertyValue = sketchLine_var->isCenterLine();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchLine_var->isCenterLine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |