# Centermarks.AddByWorkFeature Method

Parent Object: [Centermarks](../Centermarks/Centermarks.md)

## Description

Method that creates a center mark that represents the work feature within the drawing view.

## Syntax

Centermarks.**AddByWorkFeature**( ***WorkFeature*** As Object, ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant ) As [Centermark](../Centermark/Centermark.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| WorkFeature | Object | Specifies the work feature to create the center mark for. This can be a WorkPoint or WorkAxis object. In the case of a WorkAxis object, the work axis must be oriented so it is normal to the plane of the sheet. If an work axis is provided that does not meet this criteria the method will fail. |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Specifies the drawing view to create the center mark within.  When working with an assembly the input WorkPoint or WorkAxis must always be with respect to the top-level. This means that work points or axes that exist within the parts or sub-assemblies must be represented by WorkPointProxy or WorkAxisProxy objects. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the center mark. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the center mark. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
