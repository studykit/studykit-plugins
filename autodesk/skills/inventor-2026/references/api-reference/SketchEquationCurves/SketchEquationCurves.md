# SketchEquationCurves Object

## Description

The SketchEquationCurves object provides access to all the equation curves in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchEquationCurves/SketchEquationCurves_Add.md) | Creates a new sketch equation curve. |
| [IsValidExpression](../SketchEquationCurves/SketchEquationCurves_IsValidExpression.md) | Function that evaluates the provided expression and returns whether it is a valid expression or not. This can be useful when you allow the user to enter an expression and verify that it is valid before attempting to use it. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEquationCurves/SketchEquationCurves_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchEquationCurves/SketchEquationCurves_Count.md) | Gets the number of items in this collection. |
| [Item](../SketchEquationCurves/SketchEquationCurves_Item.md) | Returns the specified SketchEquationCurve object from the collection |
| [Type](../SketchEquationCurves/SketchEquationCurves_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DrawingSketch.SketchEquationCurves](../DrawingSketch/DrawingSketch_SketchEquationCurves.md), [PlanarSketch.SketchEquationCurves](../PlanarSketch/PlanarSketch_SketchEquationCurves.md), [PlanarSketchProxy.SketchEquationCurves](../PlanarSketchProxy/PlanarSketchProxy_SketchEquationCurves.md), [Sketch.SketchEquationCurves](../Sketch/Sketch_SketchEquationCurves.md), [SketchBlockDefinition.SketchEquationCurves](../SketchBlockDefinition/SketchBlockDefinition_SketchEquationCurves.md), [SketchBlockDefinitionProxy.SketchEquationCurves](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchEquationCurves.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014
