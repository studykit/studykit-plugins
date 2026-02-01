# SketchDistanceBetweenLineAndPlanarSurfaceDimension.parameter Property

Parent Object: [SketchDistanceBetweenLineAndPlanarSurfaceDimension](SketchDistanceBetweenLineAndPlanarSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object. |

"sketchDistanceBetweenLineAndPlanarSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenLineAndPlanarSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenLineAndPlanarSurfaceDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchDistanceBetweenLineAndPlanarSurfaceDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |