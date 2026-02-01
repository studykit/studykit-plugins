# Centermarks.AddByCenterOfGravity Method

Parent Object: [Centermarks](../Centermarks/Centermarks.md)

## Description

Method that creates a center mark at the center of gravity of the model in the input drawing view. This will fail in the case where the view does not contain any solid parts.

## Syntax

Centermarks.**AddByCenterOfGravity**( ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant ) As [Centermark](../Centermark/Centermark.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Specifies the view to create the center mark for. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the center mark. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the center mark. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
