# GeneralDimensions.AddRadius Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Method that creates a radius dimension.

## Syntax

GeneralDimensions.**AddRadius**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***ArrowheadsInside***] As Boolean, [***LeaderFromCenter***] As Boolean, [***Jogged***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [RadiusGeneralDimension](../RadiusGeneralDimension/RadiusGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Specifies the position of the dimension text on sheet. |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Specifies the arc or circle to dimension. A parameter along the curve should be specified in the intent. If not, a default is assumed. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| ArrowheadsInside | Boolean | Indicates whether to place the dimension line arrows inside or outside. If not specified, this argument defaults to False indicating that arrowheads will be place outside. |
| LeaderFromCenter | Boolean | Indicates whether the leader starts from the center of the arc or the circle. If not specified, the argument defaults to False indicating that the leader will not start from the center. This argument is ignored and defaulted to True if the ArrowheadsInside argument is specified to be True.   This is an optional argument whose default value is False. |
| Jogged | Boolean | Indicates whether the dimension is jogged. If not specified, the argument defaults to False.   This is an optional argument whose default value is False. |
| DimensionStyle | Variant | Specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |