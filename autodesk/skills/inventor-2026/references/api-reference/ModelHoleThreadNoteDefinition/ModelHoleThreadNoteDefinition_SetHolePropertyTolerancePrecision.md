# ModelHoleThreadNoteDefinition.SetHolePropertyTolerancePrecision Method

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Method that sets the tolerance precision for the specified hole property.

## Syntax

ModelHoleThreadNoteDefinition.**SetHolePropertyTolerancePrecision**( ***HolePropEnum*** As [HolePropertyEnum](../HolePropertyEnum.md), ***Value*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePropEnum | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum value the specifies which tolerance precision to return. Valid values are: kHoleDiameterHoleProperty, kHoleDepthHoleProperty, kCBoreDepthHoleProperty, kCBoreDiameterHoleProperty, kCSinkAngleHoleProperty, kCSinkDepthHoleProperty, kCSinkDiameterHoleProperty, kThreadDepthHoleProperty or kTapDrillDiameterHoleProperty. |
| Value | Long | Input Long value the specifies the tolerance precision. Valid value range is from 0 to 8. |

## Version

Introduced in version 2018
