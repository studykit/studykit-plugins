# GeneralDimensions.AddDiameter Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Method that creates a diameter dimension.

## Syntax

GeneralDimensions.**AddDiameter**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***ArrowheadsInside***] As Boolean, [***LeaderFromCenter***] As Boolean, [***SingleDimensionLine***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [DiameterGeneralDimension](../DiameterGeneralDimension/DiameterGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Specifies the position of the dimension text on sheet. |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Specifies the arc or circle to dimension. A parameter along the curve should be specified in the intent. If not, a default is assumed. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| ArrowheadsInside | Boolean | Indicates whether to place the dimension line arrows inside or outside. If not specified, this argument defaults to False indicating that arrowheads will be place outside. |
| LeaderFromCenter | Boolean | Indicates whether the leader starts from the center of the arc or the circle. If not specified, the argument defaults to False indicating that the leader will not start from the center.   This is an optional argument whose default value is False. |
| SingleDimensionLine | Boolean | Indicates whether to use a single dimension line. If not specified, the argument defaults to True indicating a single dimension line will be used.   This is an optional argument whose default value is True. |
| DimensionStyle | Variant | Specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11
