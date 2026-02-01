# ModelHoleThreadNoteDefinition.GetHolePropertyToleranceStatus Method

Parent Object: [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Description

Method that returns whether the tolerance for the specified hole property is enabled or not. This returns True if the hole property tolerance is enabled.

## Syntax

ModelHoleThreadNoteDefinition.**GetHolePropertyToleranceStatus**( ***HolePropEnum*** As [HolePropertyEnum](../HolePropertyEnum.md) ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePropEnum | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum value the specifies the hole property type. Valid values are: kHoleDiameterHoleProperty, kHoleDepthHoleProperty, kCBoreDepthHoleProperty, kCBoreDiameterHoleProperty, kCSinkAngleHoleProperty, kCSinkDepthHoleProperty, kCSinkDiameterHoleProperty, kThreadDepthHoleProperty or kTapDrillDiameterHoleProperty |

## Version

Introduced in version 2018
