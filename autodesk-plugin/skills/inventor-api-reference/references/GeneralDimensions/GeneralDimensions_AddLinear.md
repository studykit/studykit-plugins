# GeneralDimensions.AddLinear Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Method that creates a linear dimension. Valid intent combinations are: Two points, Two curves, Point and a curve, One linear curve, One arc curve (with DimensionType set to kAlignedDimensionType for chord length and kArcLengthDimensionType for arc length).

## Syntax

GeneralDimensions.**AddLinear**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***IntentTwo***] As Variant, [***DimensionType***] As [DimensionTypeEnum](../DimensionTypeEnum.md), [***ArrowheadsInside***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Object that specifies the position of the dimension text on sheet. |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Object that specifies the first geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| IntentTwo | Variant | Object that specifies the second geometry to dimension. This argument must be specified if the first geometry intent is a point. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | Specifies the linear dimension type. Valid values (based on the input intents) are kAlignedDimensionType, kHorizontalDimensionType, kVerticalDimensionType, kArcLengthDimensionType, kSymmetricDimensionType and kDiametricDimensionType. If not specified, the argument defaults to kAlignedDimensionType. An error will occur if the specified type is invalid for the input intents. For instance, kHorizontalDimensionType is invalid for a vertical dimension and kSymmetricDimensionType & kDiametricDimensionType are invalid if only the first intent (an edge) is specified. kArcLengthDimensionType is only valid if two intents are supplied and they represent end points of an arc or a single intent is supplied and it represents an arc.   This is an optional argument whose default value is 60161. |
| ArrowheadsInside | Boolean | Indicates whether to place the dimension line arrows inside or outside. If not specified, this argument defaults to True indicating that arrowheads will be place inside (if possible).   This is an optional argument whose default value is True. |
| DimensionStyle | Variant | Object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |