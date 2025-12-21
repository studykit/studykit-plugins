# Centerline.GetBisectorEntities Method

Parent Object: [Centerline](../Centerline/Centerline.md)

## Description

Returns the two entities that the centerline bisects. This method is only valid for kBisectorCenterline type centerlines and will fail in all other cases.

## Syntax

Centerline.**GetBisectorEntities**( ***EntityOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***EntityTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Output GeometryIntent object that provides the first entity. |
| EntityTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Output GeometryIntent object that provides the second entity. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |