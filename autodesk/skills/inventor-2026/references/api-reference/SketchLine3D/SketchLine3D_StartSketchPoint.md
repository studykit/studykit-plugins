# SketchLine3D.StartSketchPoint Property

Parent Object: [SketchLine3D](../SketchLine3D/SketchLine3D.md)

## Description

Property that returns the that defines the position of the start of the line.

## Syntax

SketchLine3D.**StartSketchPoint**() As [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md)

## Property Value

This is a read only property whose value is a [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 8
