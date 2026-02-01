# SketchDimensions.addDistanceBetweenLineAndPlanarSurfaceDimension Method

Parent Object: [SketchDimensions](SketchDimensions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensions.h>

## Description

Creates a new linear dimension controlling the distance between a sketch line and the specified planar face or construction plane. The sketch line must lie on a plane that is parallel to the planar surface. The text position is automatically chosen and is positioned so it is midway between the line and surface and the extension lines are a minimum length. You can modify the position by using functionality on the returned SketchDistanceBetweenLineAndPlanarSurfaceDimension object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.  ```` ``` #include <Fusion/Sketch/SketchDimensions.h>  // Uses no optional arguments. returnValue = sketchDimensions_var->addDistanceBetweenLineAndPlanarSurfaceDimension(line, planarSurface);  // Uses optional arguments. returnValue = sketchDimensions_var->addDistanceBetweenLineAndPlanarSurfaceDimension(line, planarSurface, isDriving); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchDistanceBetweenLineAndPlanarSurfaceDimension](SketchDistanceBetweenLineAndPlanarSurfaceDimension.htm) | Returns the newly created dimension or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The SketchLine being constrained by the dimension. |
| planarSurface | [Base](Base.htm) | The planar BRepFace or ConstructionPlane that the dimension will anchor to. |
| isDriving | boolean | Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.   This is an optional argument whose default value is True. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |