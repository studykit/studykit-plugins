# EdgeProxy.CalculateStrokesWithOptions Method

Parent Object: [EdgeProxy](../EdgeProxy/EdgeProxy.md)

## Description

Method that creates a new set of strokes within the specified conditions.

## Syntax

EdgeProxy.**CalculateStrokesWithOptions**( ***ChordalTolerance*** As Double, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***VertexCount*** As Long, ***VertexCoordinates***() As Double, ***PolylineCount*** As Long, ***PolylineLengths***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ChordalTolerance | Double | Input Double that specifies the maximum distance that the stroke can deviate from the smooth curve. This value is in centimeters. Smaller values can result in a much greater number of strokes being returned and will require more processing time to calculate. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies additional tolerances that can be used to control the output strokes. The supported options are: Name: MaxSideLength, Value: Defines the maximum side of any stroke in the polyline. A value of 0, or not supplying this value indicates that no maximum length is specified Name: MaxNormalDeviation, Value: Defines the maximum deviation between adjacent vertex normals. This value is the maximum angle allowed between normals and is input as radians. A value of 0, or not supplying this value indicates that no normal deviation is supplied. |
| VertexCount | Long | Output Long that specifies the number of vertices used to define all of the output strokes. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinate locations of the vertices. The values are defined in x, y, z order within the array and represent coordinates within the model space of the stroked object. |
| PolylineCount | Long | Output Long that specifies the number of polylines that the strokes represent. |
| PolylineLengths | Long | Output array of Longs that specifies the number of vertices that are used to define each polyline. |

## Version

Introduced in version 2017
