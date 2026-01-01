# LinearModelDimensionProxy.GetDisplayGeometry Method

Parent Object: [LinearModelDimensionProxy](../LinearModelDimensionProxy/LinearModelDimensionProxy.md)

## Description

Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids.

## Syntax

LinearModelDimensionProxy.**GetDisplayGeometry**( ***Camera*** As [Camera](../Camera/Camera.md), ***GroupCount*** As Long, ***PolylinesPerGroup***() As Long, ***FilledGroups***() As Boolean, ***PolylineCount*** As Long, ***PolylineLengths***() As Long, ***VertexCount*** As Long, ***VertexCoordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Camera | [Camera](../Camera/Camera.md) | Input Camera object that specifies the view orientation. This can either be a transient Camera object or that got from View object etc.. And the camera properties can be changed but not applied. |
| GroupCount | Long | Output Long that indicates the number of groups. A group is a set of related polylines where there can be one outer and multiple inner polylines. Groups can optionally also be filled. |
| PolylinesPerGroup | Long | Output array of Longs that indicates the number of polylines in each of the groups. The array size will be GroupCount where each value of this array indicates the number of polylines within each group. When reading the polylines within a group, the first polyline is the outer polyline and any additional closed polylines represent internal voids if the group is filled. |
| FilledGroups | Boolean | Output array of Booleans that indicates which groups are filled. A value of True indicates the corresponding group is filled. The array size will be GroupCount. If a group is filled, the first polyline in the group defines the outer loop. Any other polylines for that group represent internal loops and voids in the fill. |
| PolylineCount | Long | Output Long that indicates the total number of polylines. |
| PolylineLengths | Long | Output array of Longs that indicates the number of vertices used in each polyline. |
| VertexCount | Long | Output Long that indicates the total number of vertices. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates. |

## Version

Introduced in version 2018
