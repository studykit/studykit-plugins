# PartComponentDefinition.Sketches3D Property

Parent Object: [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md)

## Description

Property that returns the Sketches3D collection object that encapsulates all of the 3D sketches defined in this ComponentDefinition.

## Syntax

PartComponentDefinition.**Sketches3D**() As [Sketches3D](../Sketches3D/Sketches3D.md)

## Property Value

This is a read only property whose value is a [Sketches3D](../Sketches3D/Sketches3D.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Control point, equation, and intersection curve creation.](../../sample-programs/AdvancedCurveCreation_Sample.md) | This sample demonstrates several new curve creation techniques introduced in Inventor 2014. It creates a new part and then create a 2d control point spline and a 2d equation curve. Surfaces are created from these two curves by extruding them. A 3d intersection curve is created between the extrusions. A 3d control point spline and 3d equation curve are also created. |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6
