# SurfaceBody.LocateUsingPoint Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Finds the object of specified type within the proximity of the given point. By default an internal tolerance is used to gauge the proximity.

## Syntax

SurfaceBody.**LocateUsingPoint**( ***ObjectType*** As [ObjectTypeEnum](../ObjectTypeEnum.md), ***PointOnObject*** As [Point](../Point/Point.md), [***ProximityTolerance***] As Variant ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ObjectType | [ObjectTypeEnum](../ObjectTypeEnum.md) | Input ObjectType of object to find. |
| PointOnObject | [Point](../Point/Point.md) | Input . |
| ProximityTolerance | Variant | Optional input Variant that specifies the tolerance to use to test proximity. If this value is not specified, the internal tolerance is used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating flange features](../../sample-programs/FlangeDefinition_SetOffsetWidthExtent_Sample.md) | Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |