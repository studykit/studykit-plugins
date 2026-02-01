# SketchBlockDefinitionProxy.AddBySilhouette Method

Parent Object: [SketchBlockDefinitionProxy](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy.md)

## Description

Method that creates new reference sketch geometry as the silhouette on the input face near the input proximity point.

## Syntax

SketchBlockDefinitionProxy.**AddBySilhouette**( ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) ) As [SketchEntity](../SketchEntity/SketchEntity.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face that defines a silhouette edge that can be projected onto the sketch plane. |
| ProximityPoint | [Point](../Point/Point.md) | Input that identifies which one of possible multiple results to use. For example, if the input face is a cylinder there are two possible silhouette edges. |

## Version

Introduced in version 2010
