# Centermarks.Add Method

Parent Object: [Centermarks](../Centermarks/Centermarks.md)

## Description

Method that creates a center mark relative to drawing geometry. This can result in a center mark at the origin of a punch center if the specified geometry is the edge of a punch and the AtPunchCenter argument is true.

## Syntax

Centermarks.**Add**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***ExtensionLinesVisible***] As Boolean, [***AtPunchCenter***] As Boolean, [***CentermarkStyle***] As Variant, [***Layer***] As Variant ) As [Centermark](../Centermark/Centermark.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Specifies the entity to create the center mark relative to. This is typically a circular or elliptical drawing curve but can be any drawing curve when it's the edge of a punch feature and you're creating the center point at the origin of the punch. The GeometryIntent object can be created using the CreateGeometryIntent method on the Sheet object. |
| ExtensionLinesVisible | Boolean | Optional input Boolean that specifies if the extension lines should be visible in the created center mark. |
| AtPunchCenter | Boolean | Optional input Boolean that specifies if the input geometry is the edge of the punch feature the center mark should be created at the origin of the punch feature instead of the center of the input geometry.   This is an optional argument whose default value is True. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the center mark. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Object that specifies the layer to use for the center mark. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2009
