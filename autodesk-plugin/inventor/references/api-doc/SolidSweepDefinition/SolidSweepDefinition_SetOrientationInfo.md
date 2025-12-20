# SolidSweepDefinition.SetOrientationInfo Method

Parent Object: [SolidSweepDefinition](../SolidSweepDefinition/SolidSweepDefinition.md)

## Description

Method that sets the orientation info.

## Syntax

SolidSweepDefinition.**SetOrientationInfo**( ***Orientation*** As [SweepProfileOrientationEnum](../SweepProfileOrientationEnum.md), [***AlignToVector***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Orientation | [SweepProfileOrientationEnum](../SweepProfileOrientationEnum.md) | Input SweepProfileOrientationEnum to set the orientation of the sweep. |
| AlignToVector | Variant | Optional input object to specify the align to vector. This is required if the Orientation is specified to kAlignToVector. This can be a linear Edge, WorkAxis, WorkPlane or Face which can infer an axis. When a WorkPlane or planar Face object is specified, its normal is used, when a cylindrical, conical, elliptical or toroidal Face is specified its axis is used. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |