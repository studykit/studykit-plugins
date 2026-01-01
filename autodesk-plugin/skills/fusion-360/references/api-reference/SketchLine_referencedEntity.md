# SketchLine.referencedEntity Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object. |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. Ptr<Base> propertyValue = sketchLine_var->referencedEntity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |