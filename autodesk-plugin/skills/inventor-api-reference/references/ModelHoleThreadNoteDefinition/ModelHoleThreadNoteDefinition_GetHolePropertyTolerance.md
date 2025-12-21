# ModelHoleThreadNoteDefinition.GetHolePropertyTolerance Method

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Method that gets the tolerance for the specified hole property.

## Syntax

ModelHoleThreadNoteDefinition.**GetHolePropertyTolerance**( ***HolePropEnum*** As [HolePropertyEnum](../HolePropertyEnum.md) ) As [Tolerance](../Tolerance/Tolerance.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePropEnum | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum value the specifies which tolerance to return. Valid values are: kHoleDiameterHoleProperty, kHoleDepthHoleProperty, kCBoreDepthHoleProperty, kCBoreDiameterHoleProperty, kCSinkAngleHoleProperty, kCSinkDepthHoleProperty, kCSinkDiameterHoleProperty, kThreadDepthHoleProperty or kTapDrillDiameterHoleProperty. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |