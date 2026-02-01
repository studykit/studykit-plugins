# MapPointCurve.SetPositionUsingPoint Method

Parent Object: [MapPointCurve](../MapPointCurve/MapPointCurve.md)

## Description

Method that sets the position of the map point using a 3D coordinate. The index corresponds with the section of the same index. If a map point already exists for the section the input entity is a member of, the current map point will be replaced.

## Syntax

MapPointCurve.**SetPositionUsingPoint**( ***SectionIndex*** As Long, ***Position*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SectionIndex | Long | Input Long that identifies which section the map point is being defined for. The index corresponds with the section of the same index. |
| Position | [Point](../Point/Point.md) | Input that defines the coordinate position of the map point. The input point will be projected to the nearest point along the specified section. |

## Version

Introduced in version 6
