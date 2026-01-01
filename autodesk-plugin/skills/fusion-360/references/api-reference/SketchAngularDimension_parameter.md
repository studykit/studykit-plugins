# SketchAngularDimension.parameter Property

Parent Object: [SketchAngularDimension](SketchAngularDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchAngularDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object. |

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object. ```` ``` #include <Fusion/Sketch/SketchAngularDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchAngularDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |