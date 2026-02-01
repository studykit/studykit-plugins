# SketchDimensions.addEllipseMajorRadiusDimension Method

Parent Object: [SketchDimensions](SketchDimensions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensions.h>

## Description

Creates a new dimension constraint on the major radius of an ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.  ```` ``` #include <Fusion/Sketch/SketchDimensions.h>  // Uses no optional arguments. returnValue = sketchDimensions_var->addEllipseMajorRadiusDimension(ellipse, textPoint);  // Uses optional arguments. returnValue = sketchDimensions_var->addEllipseMajorRadiusDimension(ellipse, textPoint, isDriving); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm) | Returns the newly created dimension or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ellipse | [SketchCurve](SketchCurve.htm) | The SketchEllipse to dimension. |
| textPoint | [Point3D](Point3D.htm) | A Point3D object that defines the position of the dimension text. |
| isDriving | boolean | Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchDimensions.AddEllipseMajorRadiusDimension](SketchDimension_addEllipseMajorRadiusDimension_Sample.htm) | Demonstrates the SketchDimension.addEllipseMajorRadiusDimension method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |