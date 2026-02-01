# SketchArc.nativeObject Property

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a SketchArc object. |

"sketchArc\_var" is a variable referencing a SketchArc object. ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Get the value of the property. Ptr<SketchArc> propertyValue = sketchArc_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchArc](SketchArc.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |