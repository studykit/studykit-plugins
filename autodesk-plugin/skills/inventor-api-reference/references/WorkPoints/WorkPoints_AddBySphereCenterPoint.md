# WorkPoints.AddBySphereCenterPoint Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Creates a new work point at the center of the sphere specified by the input face. This method is not currently supported when creating a work point within an assembly.

## Syntax

WorkPoints.**AddBySphereCenterPoint**( ***Face*** As [Face](../Face/Face.md), [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object whose geometry is a spherical surface. An error occurs if the geometry of the input face is not a spherical surface. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |