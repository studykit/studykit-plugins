# SketchLinearDimension.attributes Property

Parent Object: [SketchLinearDimension](SketchLinearDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDimension.h>

## Description

Returns the collection of attributes associated with this sketch dimension.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. |

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDimension.h>  // Get the value of the property. Ptr<Attributes> propertyValue = sketchLinearDimension_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |