# SketchControlPointSplines3D Object

## Description

The SketchControlPointSplines3D object supports the creation of new control point splines and provides access to all the control point splines in a 3D sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchControlPointSplines3D/SketchControlPointSplines3D_Add.md) | Method that creates a control point spline based on the set of input points that define the vertices of the control polygon. A closed spline is created when the start and end points have the same coordinate. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchControlPointSplines3D/SketchControlPointSplines3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchControlPointSplines3D/SketchControlPointSplines3D_Count.md) | Gets the number of items in this collection. |
| [Item](../SketchControlPointSplines3D/SketchControlPointSplines3D_Item.md) | Method that returns the specified SketchControlPointSpline3D object from the collection. |
| [Type](../SketchControlPointSplines3D/SketchControlPointSplines3D_Type.md) | Read-only property returning kSketchControlPointSplinesObject indicating the type of object. |

## Accessed From

[Sketch3D.SketchControlPointSplines3D](../Sketch3D/Sketch3D_SketchControlPointSplines3D.md), [Sketch3DProxy.SketchControlPointSplines3D](../Sketch3DProxy/Sketch3DProxy_SketchControlPointSplines3D.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |

## Version

Introduced in version 2014
