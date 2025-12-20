# SurfaceBody.IsPointInside Property

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Property that returns a constant indicating whether the specified point is inside, on or outside the body.

## Syntax

SurfaceBody.**IsPointInside**( ***Point***() As Double, [***UseBox***] As Boolean ) As [ContainmentEnum](../ContainmentEnum.md)

## Property Value

This is a read only property whose value is a [ContainmentEnum](../ContainmentEnum.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Double | Point whose location to determine. |
| UseBox | Boolean | Optional input Boolean that specifies whether to use a box to determine if the point is inside, on or outside of the body. Sometimes one wants to avoid the creation of bounding boxes during intermediate steps of a construction because the creation of bounding boxes can be costly. If you're applying multiple operations to a body then the bounding box of some of the shells would be invalid after each operation. You wouldn't want to use the bounding box during these intermediate stages because you might spend more time computing the bounding box than you'd save by using it for trivial rejection. On the other hand, if you have a stable body and a high likelihood that the bounding box is up-to-date, then it might save some time to set the use\_box parameter to true. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |