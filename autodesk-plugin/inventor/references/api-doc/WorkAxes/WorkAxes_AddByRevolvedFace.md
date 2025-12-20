# WorkAxes.AddByRevolvedFace Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis through the axis of a revolved face. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByRevolvedFace**( ***Face*** As [Face](../Face/Face.md), [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object whose geometry is a revolved surface. Valid surface types include cylinders, cones, and toroids. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |