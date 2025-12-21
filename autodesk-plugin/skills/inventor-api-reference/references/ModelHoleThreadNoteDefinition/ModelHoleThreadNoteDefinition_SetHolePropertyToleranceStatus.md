# ModelHoleThreadNoteDefinition.SetHolePropertyToleranceStatus Method

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Method that enables/disables the tolerance for the specified hole property.

## Syntax

ModelHoleThreadNoteDefinition.**SetHolePropertyToleranceStatus**( ***HolePropEnum*** As [HolePropertyEnum](../HolePropertyEnum.md), ***Value*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePropEnum | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum value the specifies hole property type. Valid values are: kHoleDiameterHoleProperty, kHoleDepthHoleProperty, kCBoreDepthHoleProperty, kCBoreDiameterHoleProperty, kCSinkAngleHoleProperty, kCSinkDepthHoleProperty, kCSinkDiameterHoleProperty, kThreadDepthHoleProperty or kTapDrillDiameterHoleProperty. |
| Value | Boolean | Input Boolean value the specifies the enabled status of the hole property tolerance. |

## Version

Introduced in version 2018
