# RibDefinition.GetThicknessPlane Method

Parent Object: [RibDefinition](../RibDefinition/RibDefinition.md)

## Description

Method that gets the plane at which the input thickness is held.

## Syntax

RibDefinition.**GetThicknessPlane**( ***HoldThicknessAt*** As [RibThicknessPlaneEnum](../RibThicknessPlaneEnum.md), ***NeutralGeometry*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HoldThicknessAt | [RibThicknessPlaneEnum](../RibThicknessPlaneEnum.md) | Output RibThicknessPlaneEnum that defines the plane at which the thickness should be held. Valid returns values are kRibThicknessAtSketchPlane, kRibThicknessAtRoot and kRibThicknessAtNeutralGeometry. If kRibThicknessAtNeutralGeometry is returned, the NeutralGeometry argument returns the correposnig geometry. |
| NeutralGeometry | Object | Output object that specifies the neutral geometry if the HoldThicknessAt argument returns kRibThicknessAtNeutralGeometry. Else, this argument returns Nothing. |

## Version

Introduced in version 2012
