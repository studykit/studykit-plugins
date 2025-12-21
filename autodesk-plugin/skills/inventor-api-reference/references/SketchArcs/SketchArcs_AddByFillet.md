# SketchArcs.AddByFillet Method

Parent Object: [SketchArcs](../SketchArcs/SketchArcs.md)

## Description

Method that creates a new sketch arc as a fillet between two sketch entities.

## Syntax

SketchArcs.**AddByFillet**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***Radius*** As Variant, ***PointOnEntityOne*** As [Point2d](../Point2d/Point2d.md), ***PointOnEntityTwo*** As [Point2d](../Point2d/Point2d.md) ) As [SketchArc](../SketchArc/SketchArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |
| Radius | Variant | Input double that defines the radius of the arc in centimeters. |
| PointOnEntityOne | [Point2d](../Point2d/Point2d.md) | Input that defines the point on the first entity on which to start the SketchArc. |
| PointOnEntityTwo | [Point2d](../Point2d/Point2d.md) | Input that defines the point on the second entity on which to end the SketchArc. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5.3
