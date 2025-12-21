# TransientBRep.CreateSilhouetteCurve Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that calculates the silhouette curve geometry for a given face as viewed from a given direction.

## Remarks

The result is a SurfaceBody object that will contain one or more Wire objects that represent the silhouette curve(s). This method can return Nothing in the case where there is not a silhouette curve for the specified face.

## Syntax

TransientBRep.**CreateSilhouetteCurve**( ***Face*** As [Face](../Face/Face.md), ***ViewDirection*** As [UnitVector](../UnitVector/UnitVector.md), ***ReturnCoincidentSilhouettes*** As Boolean ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object to calculate the silhouette curve for. |
| ViewDirection | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that defines the view direction to calculate the silhouette curve relative to. The silhouette curve will lie on the input where the face normal is perpendicular to the view direction. |
| ReturnCoincidentSilhouettes | Boolean | Input Boolean that specifies if silhouette curves that are coincident to the edges of the face should be returned or not. If True, these curves will be returned. |

## Version

Introduced in version 2009
