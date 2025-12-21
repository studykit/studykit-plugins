# GeneralDimensions.AddAngular Method

Parent Object: [GeneralDimensions](../GeneralDimensions/GeneralDimensions.md)

## Description

Method that creates an angular dimension. Valid intent combinations are Three points, Two non-parallel linear curves, One arc curve.

## Syntax

GeneralDimensions.**AddAngular**( ***TextOrigin*** As [Point2d](../Point2d/Point2d.md), ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***IntentTwo***] As Variant, [***IntentThree***] As Variant, [***ArrowheadsInside***] As Boolean, [***UseQuadrant***] As Boolean, [***OppositeAngle***] As Boolean, [***DimensionStyle***] As Variant, [***Layer***] As Variant ) As [AngularGeneralDimension](../AngularGeneralDimension/AngularGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextOrigin | [Point2d](../Point2d/Point2d.md) | Object that specifies the position of the dimension text on sheet. |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Object that specifies the first geometry to dimension. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| IntentTwo | Variant | Object that specifies the second geometry to dimension. If three point intents are provided, this input indicates the apex point of the angle. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| IntentThree | Variant | Object that specifies the third geometry to dimension. This argument must be specified if the first and second geometry intents are points. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object.   This is an optional argument whose default value is null. |
| ArrowheadsInside | Boolean | Indicates whether to place the dimension line arrows inside or outside. If not specified, this argument defaults to True indicating that arrowheads will be place inside (if possible).   This is an optional argument whose default value is True. |
| UseQuadrant | Boolean | Optional input Boolean that indicates whether to use the quadrant in which the input text point lies to decide which angle to dimension. If not specified, the argument defaults to True. If a single (arc) intent is provided as input, this argument is ignored and assumed to be False.   This is an optional argument whose default value is True. |
| OppositeAngle | Boolean | Indicates whether to dimension the opposite angle. If not specified, the argument defaults to False.   This is an optional argument whose default value is False. |
| DimensionStyle | Variant | Object that specifies the dimension style to use for the dimension. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Object that specifies the layer to use for the dimension. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11
