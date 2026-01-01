# SketchLine.nativeObject Property

Parent Object: [SketchLine](SketchLine.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLine.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLine\_var" is a variable referencing a SketchLine object. |

"sketchLine\_var" is a variable referencing a SketchLine object. ```` ``` #include <Fusion/Sketch/SketchLine.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = sketchLine_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |