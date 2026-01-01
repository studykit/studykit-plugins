# SketchText.boundaryLines Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This was retired when Fusion added support for sketch along a curve, which doesn't have the boundary lines. This functionality is replaced by the MultiLineTextDefinition.rectangleLines property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object.  ```` ``` # Get the value of the property. propertyValue = sketchText_var.boundaryLines ``` ```` |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. Ptr<SketchLineList> propertyValue = sketchText_var->boundaryLines(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLineList](SketchLineList.htm).

## Version

Introduced in version March 2015
Retired in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |