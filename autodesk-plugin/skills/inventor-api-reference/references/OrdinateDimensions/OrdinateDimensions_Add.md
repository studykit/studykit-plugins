# OrdinateDimensions.Add Method

Parent Object: [OrdinateDimensions](../OrdinateDimensions/OrdinateDimensions.md)

## Description

Method that creates an ordinate dimension.

## Remarks

The ordinate dimension will be placed with respect to an origin point defined on the view. If an origin point has not been already defined on the view, this method will fail. The DrawingView.HasOriginIndicator property can be used to verify if the origin has already been created. If it has not been created, the DrawingView.CreateOriginIndicator method can be used to create it. The difference in behavior when placing ordinate dimensions using the API (when compared to placing them interactively using the user interface) is that ordinate dimensions have to be placed only one at a time using the API. To illustrate this difference, consider the drawing view shown in the figure below which shows ordinate dimensions placed on a curve.

![](../images/OrdinateDimensions_Add_OrdinateDimensionsPlacedOnACurve.png)

**Ordinate dimensions placed on a curve**

The figure shows three ordinate dimensions placed on the start point, center point and end point of the curve. When using the user interface, all three dimensions can be placed at the same time by starting the ordinate dimension command and just selecting the curve entity (assuming that the origin for the ordinate dimensions has already been selected, otherwise this has to be selected first). After the dimensions have been placed, each one of them can be edited or deleted individually. Therefore, these dimensions are independent without any relationship or grouping between them. Similarly, if the line is selected for placing ordinate dimensions, two ordinate dimensions will be placed at the start point and end point of the line respectively. The user interface merely allows the convenience of placing multiple dimensions simultaneously, although they are independent. When placing these ordinate dimensions using the API, they can only be placed one at a time. If the three dimensions shown in the figure need to be placed using the API, this method needs to be called three times and the start point, center point and end point of the curve has to be specified as input geometry intent. Therefore, the only acceptable input geometry intent for placing an ordinate dimension is a point to which the ordinate dimension can be attached.

## Syntax

OrdinateDimensions.**Add**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***DimensionType*** As [DimensionTypeEnum](../DimensionTypeEnum.md), [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [OrdinateDimension](../OrdinateDimension/OrdinateDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the geometry to dimension. The GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. Valid intent values are points that specify geometry to which an ordinate dimension can be attached. For example, the start, mid, end point of lines and start, end, center point of curves are valid intent values. If an invalid intent is specified, this method will fail. |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the dimension text on the sheet. The specified position of the dimension text together with the dimension alignment type (specified by the DimensionType argument) will determine the actual resulting position for the dimension text. If the specified dimension text position lies along the dimension line implied by the DimensionType argument, the dimension text will be placed exactly at the specified position. On the other hand, if the specified dimension text position does not lie along the dimension line implied by the DimensionType argument, the specified point will be projected onto the dimension line and the dimension text will be placed at this projected point. The following figures show how the specified position will be interpreted. In the first figure, the dimension type is specified to be a horizontal ordinate dimension and the specified point (P) lies on the horizontal line (L), therefore the dimension text will be placed exactly at the specified point (P).     ![](../images/OrdinateDimensions_Add_TextOrigin_PointOnTheLine.png)    In the second figure (shown below), the dimension type is specified to be a horizontal ordinate dimension and the specified point (P) does not lie on the horizontal line (L), therefore the point P will be first projected onto the dimension line and this projected point (P') will be used as the placement point for the dimension text.     ![](../images/OrdinateDimensions_Add_TextOrigin_PointNotOnTheLine.png) |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | Input DimensionTypeEnum that specifies the ordinate dimension type. Valid values kHorizontalDimensionType, kVerticalDimensionType and kAlignedDimensionType. The value kAlignedDimensionType can be specified only if the geometry of the specified input intent represents a line in which case an ordinate dimension that is aligned along the direction of the line will be created. An error will occur if an invalid dimension type is specified. For instance, kArcLengthDimensionType, kDiametricDimensionType and kSymmetricDimensionType are invalid for all types of intent and kAlignedDimensionType is invalid if the geometry of the specified input intent does not represent a line. The following figures show the aligned, horizontal and vertical ordinate dimensions for the same input intent (the geometry of the intent represents a line whose direction is used to place the aligned ordinate dimension).  **Aligned Ordinate Dimension** ![](../images/OrdinateDimensions_Add_DimensionType_AlignedOrdinateDimension.png) **Horizontal Ordinate Dimension** ![](../images/OrdinateDimensions_Add_DimensionType_HorizontalOrdinateDimension.png) **Vertical Ordinate Dimension** ![](../images/OrdinateDimensions_Add_DimensionType_VerticalOrdinateDimension.png) |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create ordinate dimension](../../sample-programs/OrdinateDimensions_Add_Sample.md) | This sample demonstrates the creation of ordinate dimensions in a drawing document. |

## Version

Introduced in version 2009
