# RevisionCloudControlPoints.Add Method

Parent Object: [RevisionCloudControlPoints](../RevisionCloudControlPoints/RevisionCloudControlPoints.md)

## Description

Method that creates a new RevisionCloudControlPoint.

## Syntax

RevisionCloudControlPoints.**Add**( ***Position*** As [Point2d](../Point2d/Point2d.md), [***TargetIndex***] As Variant, [***After***] As Boolean ) As [RevisionCloudControlPoint](../RevisionCloudControlPoint/RevisionCloudControlPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position for a new revision cloud control point. |
| TargetIndex | Variant | Optional input Long value that specifies the target index of the RevisionCloudControlPoint to add a new one next to. If not provided, default value 0 will be used which indicates the new control point will be added as the last one. |
| After | Boolean | Optional input Boolean value that specifies whether the new added control point will be placed after the target index of the RevisionCloudControlPoint. If not provided this defaults to True.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2024
