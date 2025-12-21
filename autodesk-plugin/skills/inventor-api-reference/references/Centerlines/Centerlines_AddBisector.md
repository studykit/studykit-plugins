# Centerlines.AddBisector Method

Parent Object: [Centerlines](../Centerlines/Centerlines.md)

## Description

Method that creates a new bisector centerline. The centerline created with this method is kBisectorCenterline type.

## Syntax

Centerlines.**AddBisector**( ***EntityOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***EntityTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant ) As [Centerline](../Centerline/Centerline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent that defines the first entity to bisect. This can be a line or a circular entity. |
| EntityTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent that defines the second entity to bisect. If the first entity was a line then this must also be a line. If the first entity was a circular entity then this must be a circular entity that is concentric to the first entity. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the centerline. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the centerline. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2009
