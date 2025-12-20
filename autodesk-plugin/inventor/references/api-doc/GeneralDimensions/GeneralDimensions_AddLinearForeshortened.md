# GeneralDimensions.AddLinearForeshortened Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Creates a linear foreshortened dimension on the drawing sheet.

## Syntax

GeneralDimensions.**AddLinearForeshortened**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***IntentTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***HideSecondArrowhead***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the dimension text on sheet. |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the first geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| IntentTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the second geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| HideSecondArrowhead | Boolean | Optional input Boolean that specifies whether hide the second arrowhead of the dimension. |
| DimensionStyle | Variant | Optional input DimensionStyle object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create linear foreshortened dimension sample](../../sample-programs/CreateLinearForeshortenedDimSample_Sample.md) | This sample demonstrates the creation of a linear foreshortened dimension. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |