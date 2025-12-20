# Balloon.SetBalloonType Method

Parent Object: [Balloon](../Balloon/Balloon.md)

## Description

Method that sets the balloon type.

## Syntax

Balloon.**SetBalloonType**( ***BalloonType*** As [BalloonTypeEnum](../BalloonTypeEnum.md), [***BalloonTypeData***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BalloonType | [BalloonTypeEnum](../BalloonTypeEnum.md) | Constant that indicates the balloon type. Valid types are kCircularWithOneEntryBalloonType, kCircularWithTwoEntriesBalloonType, kHexagonBalloonType, kLinearBalloonType, kNoneBalloonType and kSketchedSymbolBalloonType. Setting the type to kNoneBalloonType specifies that all the properties chosen in the style will be displayed. |
| BalloonTypeData | Variant | Optional input data associated with certain balloon types. If the balloon type is kSketchedSymbolBalloonType, this argument requires a SketchedSymbolDefinition object. Else, this argument is ignored. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Balloons - edit](../../sample-programs/Balloons_Sample.md) | This sample demonstrates the editing of balloons in a drawing. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |