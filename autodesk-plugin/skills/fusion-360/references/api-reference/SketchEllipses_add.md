# SketchEllipses.add Method

Parent Object: [SketchEllipses](SketchEllipses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipses.h>

## Description

Creates a sketch ellipse using the center point, a point defining the major axis and a third point anywhere along the ellipse. The created ellipse is parallel to the x-y plane of the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipses\_var" is a variable referencing a [SketchEllipses](SketchEllipses.htm) object.```` ``` returnValue = sketchEllipses_var.add(centerPoint, majorAxisPoint, point) ``` ```` |

"sketchEllipses\_var" is a variable referencing a [SketchEllipses](SketchEllipses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEllipse](SketchEllipse.htm) | Returns the newly created SketchEllipse object if the creation was successful or null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| centerPoint | [Base](Base.htm) | The center point of the ellipse. This can be either an existing SketchPoint or a Point3D object. |
| majorAxisPoint | [Point3D](Point3D.htm) | A point3D object that defines both the major axis direction and major axis radius. |
| point | [Point3D](Point3D.htm) | A point3D object that the ellipse will pass through. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchDimensions.AddEllipseMajorRadiusDimension](SketchDimension_addEllipseMajorRadiusDimension_Sample.htm) | Demonstrates the SketchDimension.addEllipseMajorRadiusDimension method. |
| [SketchDimensions.AddEllipseMinorRadiusDimension](SketchDimension_addEllipseMinorRadiusDimension_Sample.htm) | Demonstrates the SketchDimension.addEllipseMinorRadiusDimension method. |
| [SketchEllipses.add](SketchEllipses_add_Sample.htm) | Demonstrates the SketchEllipses.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |