# SilhouetteCurves.AddSilhouette Method

Parent Object: [SilhouetteCurves](../SilhouetteCurves/SilhouetteCurves.md)

## Description

Method that creates a silhouette curve.

## Syntax

SilhouetteCurves.**AddSilhouette**( ***Body*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***DirectionEntity*** As Object, [***ExcludedFaces***] As Variant, [***ExcludeStraightFaces***] As Variant, [***ExcludeInteralFaces***] As Variant ) As [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Body | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody that defines the surfaces to project the silhouette curve from. |
| DirectionEntity | Object | Input entity that defines the direction used to calculate the silhouette curve. Valid input is a planar face or work plane (the normal of the face or work plane is used), a cylindrical/conical face (the axis is used), a work axis, or a linear edge. |
| ExcludedFaces | Variant | Optional input FaceCollection that specifies the faces that are excluded in the silhouette curve projection. |
| ExcludeStraightFaces | Variant | Optional input Boolean that specifies whether to exclude the faces that are perpendicular to the project direction from the silhouette curve projection.   This is an optional argument whose default value is null. |
| ExcludeInteralFaces | Variant | Optional input Boolean that specifies whether to exclude the internal faces from the silhouette curve projection.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2021
