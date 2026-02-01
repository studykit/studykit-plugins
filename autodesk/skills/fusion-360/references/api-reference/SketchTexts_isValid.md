# SketchTexts.isValid Property

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a SketchTexts object. |

"sketchTexts\_var" is a variable referencing a SketchTexts object. ```` ``` #include <Fusion/Sketch/SketchTexts.h>  // Get the value of the property. boolean propertyValue = sketchTexts_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |