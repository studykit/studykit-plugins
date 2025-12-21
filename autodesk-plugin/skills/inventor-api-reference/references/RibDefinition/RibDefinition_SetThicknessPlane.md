# RibDefinition.SetThicknessPlane Method

Parent Object: [RibDefinition](../RibDefinition/RibDefinition.md)

## Description

Method that sets the plane at which the input thickness is held.

## Syntax

RibDefinition.**SetThicknessPlane**( ***HoldThicknessAt*** As [RibThicknessPlaneEnum](../RibThicknessPlaneEnum.md), [***NeutralGeometry***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HoldThicknessAt | [RibThicknessPlaneEnum](../RibThicknessPlaneEnum.md) | Input RibThicknessPlaneEnum that defines the plane at which the thickness should be held. Valid inputs are kRibThicknessAtSketchPlane, kRibThicknessAtRoot and kRibThicknessAtNeutralGeometry. If kRibThicknessAtNeutralGeometry is provided as input, the NeutralGeometry argument must also be provided, else the method will fail. |
| NeutralGeometry | Variant | Optional input object that specifies the neutral geometry if the HoldThicknessAt argument is specified to be kRibThicknessAtNeutralGeometry. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |