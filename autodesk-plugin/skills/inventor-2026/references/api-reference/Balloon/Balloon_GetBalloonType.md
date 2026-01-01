# Balloon.GetBalloonType Method

Parent Object: [Balloon](../Balloon/Balloon.md)

## Description

Method that gets the balloon type.

## Syntax

Balloon.**GetBalloonType**( ***BalloonType*** As [BalloonTypeEnum](../BalloonTypeEnum.md), ***BalloonTypeData*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BalloonType | [BalloonTypeEnum](../BalloonTypeEnum.md) | Gets the constant that indicates the balloon type. Valid types are kCircularWithOneEntryBalloonType, kCircularWithTwoEntriesBalloonType, kHexagonBalloonType, kLinearBalloonType, kNoneBalloonType and kSketchedSymbolBalloonType. |
| BalloonTypeData | Variant | Returns the data associated with certain balloon types. If the balloon type is kSketchedSymbolBalloonType, this returns a SketchedSymbol object. Else, this returns Nothing. |

## Version

Introduced in version 9
