# Sketch3D.SketchLines3D Property

Parent Object: [Sketch3D](../Sketch3D/Sketch3D.md)

## Description

Property that returns the SketchLines3D collection object. This collection provides access to the existing lines in the sketch and provides functionality to create new lines.

## Syntax

Sketch3D.**SketchLines3D**() As [SketchLines3D](../SketchLines3D/SketchLines3D.md)

## Property Value

This is a read only property whose value is a [SketchLines3D](../SketchLines3D/SketchLines3D.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6
