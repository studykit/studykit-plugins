# PatternBoundarySetting.GetBoundarySettingData Method

Parent Object: [PatternBoundarySetting](../PatternBoundarySetting/PatternBoundarySetting.md)

## Description

Method that gets the boundary setting data.

## Syntax

PatternBoundarySetting.**GetBoundarySettingData**( ***Boundary*** As Object, ***BoundaryInclusionType*** As [PatternBoundaryInclusionEnum](../PatternBoundaryInclusionEnum.md), ***OccurrenceBasePoint*** As Object, ***Offset*** As Double, ***OffsetFlipped*** As Boolean, ***Reserved*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Boundary | Object | Output object that indicate the boundary for the pattern feature. This can be a FaceCollection object containing planar Face objects or a Profile object. |
| BoundaryInclusionType | [PatternBoundaryInclusionEnum](../PatternBoundaryInclusionEnum.md) | Output PatternBoundaryInclusionEnum that indicates the boundary inclusion type. |
| OccurrenceBasePoint | Object | Output point indicating the occurrence base point position. This can be a WorkPoint, Vertex or GeometryIntent indicating the mid point of an edge or center of circular/elliptical edge. When the BoundaryInclusionType does not return kOccurrenceBasePointInclusionType this returns Nothing. |
| Offset | Double | Output Double value indicating the offset value. |
| OffsetFlipped | Boolean | Output Boolean value that indicates whether the offset is flipped or not. |
| Reserved | Variant | Reserved argument for future use . |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |