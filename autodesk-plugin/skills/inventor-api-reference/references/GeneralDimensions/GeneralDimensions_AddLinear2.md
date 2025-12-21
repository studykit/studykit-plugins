# GeneralDimensions.AddLinear2 Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Creates a linear dimension on the drawing sheet.

## Syntax

GeneralDimensions.**AddLinear2**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***IntentTwo***] As Variant, [***DimensionType***] As [DimensionTypeEnum](../DimensionTypeEnum.md), [***AlignmentGeometry***] As Variant, [***ArrowheadsInside***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the dimension text on sheet. |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the first geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| IntentTwo | Variant | Optional input GeometryIntent object that specifies the second geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | Optional input DimensionTypeEnum that specifies the linear dimension type. Valid values (based on the input intents) are kAlignedDimensionType, kHorizontalDimensionType, kVerticalDimensionType, kArcLengthDimensionType, kSymmetricDimensionType, kDiametricDimensionType, kAlignedToCurveDimensionType and kNormalToCurveDimensionType. If not specified, the argument defaults to kAlignedDimensionType. An error will occur if the specified type is invalid for the input intents. For instance, kHorizontalDimensionType is invalid for a vertical dimension and kSymmetricDimensionType & kDiametricDimensionType are invalid if only the first intent (an edge) is specified. kArcLengthDimensionType is only valid if two intents are supplied and they represent end points of an arc or a single intent is supplied and it represents an arc.   This is an optional argument whose default value is 60161. |
| AlignmentGeometry | Variant | Optional input linear geometry object to align the dimension. Valid objects are DrawingCurve and SketchLine in the same DrawingView as the dimension. This is only applicable if the DimensionType is set to kAlignedToCurveDimensionType or kNormalToCurveDimensionType.   This is an optional argument whose default value is null. |
| ArrowheadsInside | Boolean | Optional input Boolean that indicates whether to place the dimension line arrows inside or outside. If not specified, this argument defaults to True indicating that arrowheads will be place inside (if possible).   This is an optional argument whose default value is True. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |