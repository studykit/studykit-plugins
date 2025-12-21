# SketchControlPointSplines Object

## Description

The SketchControlPointSplines object supports creating new control point splines and provides access to all the existing control point splines in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchControlPointSplines/SketchControlPointSplines_Add.md) | Method that creates a control point spline based on the set of input points that define the vertices of the control polygon. A closed spline is created when the start and end points have the same coordinate. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchControlPointSplines/SketchControlPointSplines_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchControlPointSplines/SketchControlPointSplines_Count.md) | Gets the number of items in this collection. |
| [Item](../SketchControlPointSplines/SketchControlPointSplines_Item.md) | Returns the specified SketchControlPointSpline object from the collection. |
| [Type](../SketchControlPointSplines/SketchControlPointSplines_Type.md) | Read-only property returning kSketchControlPointSplinesObject indicating the type of object. |

## Accessed From

[DrawingSketch.SketchControlPointSplines](../DrawingSketch/DrawingSketch_SketchControlPointSplines.md), [PlanarSketch.SketchControlPointSplines](../PlanarSketch/PlanarSketch_SketchControlPointSplines.md), [PlanarSketchProxy.SketchControlPointSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchControlPointSplines.md), [Sketch.SketchControlPointSplines](../Sketch/Sketch_SketchControlPointSplines.md), [SketchBlockDefinition.SketchControlPointSplines](../SketchBlockDefinition/SketchBlockDefinition_SketchControlPointSplines.md), [SketchBlockDefinitionProxy.SketchControlPointSplines](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchControlPointSplines.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |