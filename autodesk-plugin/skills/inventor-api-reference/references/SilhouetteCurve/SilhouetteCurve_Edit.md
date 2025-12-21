# SilhouetteCurve.Edit Method

Parent Object: [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md)

## Description

Method that edits all of the inputs used to compute the silhouette curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit.

## Syntax

SilhouetteCurve.**Edit**( ***FacesOrBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***DirectionEntity*** As Object, [***ExcludedFaces***] As Variant, [***ExcludeStraightFaces***] As Variant, [***ExcludeInternalFaces***] As Variant ) As [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FacesOrBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) |  |
| DirectionEntity | Object |  |
| ExcludedFaces | Variant |  |
| ExcludeStraightFaces | Variant | This is an optional argument whose default value is null. |
| ExcludeInternalFaces | Variant | This is an optional argument whose default value is null. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |