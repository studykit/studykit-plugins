# Centerlines.AddByWorkFeature Method

Parent Object: [Centerlines](../Centerlines/Centerlines.md)

## Description

Method that creates a center line that represents the work feature within the drawing view.

## Syntax

Centerlines.**AddByWorkFeature**( ***WorkFeature*** As Object, ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), [***CentermarkStyle***] As Variant, [***Layer***] As Variant ) As [Centerline](../Centerline/Centerline.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| WorkFeature | Object | Specifies the work feature to create the center line for. This can be a WorkAxis or WorkPlane object. In the case of a WorkPlane object, the work plane must be oriented so it is perpendicular to the plane of the sheet, (only the edge of the work plane is visible within that view). If an work plane is provided that does not meet this criteria the method will fail.  When working with an assembly the input WorkAxis or WorkPlane must always be with respect to the top-level. This means that work points or axes that exist within the parts or sub-assemblies must be represented by WorkAxisProxy or WorkPlaneProxy objects. |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Specifies the drawing view to create the centerline within. |
| CentermarkStyle | Variant | Object that specifies the center mark style to use for the centerline. If not specified, the style defined by the active standard is used. |
| Layer | Variant | Object that specifies the layer to use for the centerline. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
