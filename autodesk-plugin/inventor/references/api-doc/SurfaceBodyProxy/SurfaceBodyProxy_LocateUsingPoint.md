# SurfaceBodyProxy.LocateUsingPoint Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Finds the object of specified type within the proximity of the given point. By default an internal tolerance is used to gauge the proximity.

## Syntax

SurfaceBodyProxy.**LocateUsingPoint**( ***ObjectType*** As [ObjectTypeEnum](../ObjectTypeEnum.md), ***PointOnObject*** As [Point](../Point/Point.md), [***ProximityTolerance***] As Variant ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ObjectType | [ObjectTypeEnum](../ObjectTypeEnum.md) | Input ObjectType of object to find. |
| PointOnObject | [Point](../Point/Point.md) | Input . |
| ProximityTolerance | Variant | Optional input Variant that specifies the tolerance to use to test proximity. If this value is not specified, the internal tolerance is used. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |