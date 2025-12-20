# SketchEquationCurves3D Object

## Description

The SketchEquationCurves3D object provides access to all the equation curves in a 3D sketch and supports the ability to create new equation curves.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchEquationCurves3D/SketchEquationCurves3D_Add.md) | Creates a new sketch equation curve in a 3D sketch. |
| [IsValidExpression](../SketchEquationCurves3D/SketchEquationCurves3D_IsValidExpression.md) | Function that evaluates the provided expression and returns whether it is a valid expression or not. This can be useful when you allow the user to enter an expression and verify that it is valid before attempting to use it. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEquationCurves3D/SketchEquationCurves3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchEquationCurves3D/SketchEquationCurves3D_Count.md) | Gets the number of items in this collection. |
| [Item](../SketchEquationCurves3D/SketchEquationCurves3D_Item.md) | Method that returns the specified SketchEquationCurve3D object from the collection. |
| [Type](../SketchEquationCurves3D/SketchEquationCurves3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.SketchEquationCurves3D](../Sketch3D/Sketch3D_SketchEquationCurves3D.md), [Sketch3DProxy.SketchEquationCurves3D](../Sketch3DProxy/Sketch3DProxy_SketchEquationCurves3D.md)

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