# SketchCurve.isLinked Property

Parent Object: [SketchCurve](SketchCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurve\_var" is a variable referencing a SketchCurve object. |

"sketchCurve\_var" is a variable referencing a SketchCurve object. ```` ``` #include <Fusion/Sketch/SketchCurve.h>  // Get the value of the property. boolean propertyValue = sketchCurve_var->isLinked(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |