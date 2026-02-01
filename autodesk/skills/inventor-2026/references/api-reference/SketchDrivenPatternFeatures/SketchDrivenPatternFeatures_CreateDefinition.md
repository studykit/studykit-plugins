# SketchDrivenPatternFeatures.CreateDefinition Method

Parent Object: [SketchDrivenPatternFeatures](../SketchDrivenPatternFeatures/SketchDrivenPatternFeatures.md)

## Description

Method that creates a new sketch driven pattern feature definition.

## Syntax

SketchDrivenPatternFeatures.**CreateDefinition**( ***ParentFeatures*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Sketch*** As Object, [***BasePoint***] As Variant, [***ReferenceFaces***] As Variant ) As [SketchDrivenPatternDefinition](../SketchDrivenPatternDefinition/SketchDrivenPatternDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentFeatures | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the features to be patterned. The collection could contain the various part features, sheet metal features, work planes, work axes, work points, or a SurfaceBody. If a SurfaceBody is supplied, the only other objects that can be in the collection are work features and surface part features. |
| Sketch | Object | Input PlanarSketch or Sketch3D object that contains the sketch points to locate the pattern occurrences. |
| BasePoint | Variant | Optional input object that indicates the position of base point. This can be a SketchPoint, SketchPoint3D, WorkPoint, or GeometryIntent that indicates a point on geometry. If a GeometryIntent is provided, you can specify the mid-point of sketch line, start/end/mid-point of a linear edge, the center of a circular/elliptical edge, planar face center, the start/mid/end point of the axis of a cylindrical/conical face, or the center of torus/spherical face. |
| ReferenceFaces | Variant | Optional input FaceCollection that specifies the reference faces.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2017
