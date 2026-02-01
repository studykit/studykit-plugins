# DSValueGraph.SetSegmentInterpolationType Method

Parent Object: [DSValueGraph](../DSValueGraph/DSValueGraph.md)

## Description

Sets the interpolation method used for the specified curve segment. A curve segment is defined as the curve between two of the value points. There are PointCount-1 segments.

## Syntax

DSValueGraph.**SetSegmentInterpolationType**( ***SegmentIndex*** As Long, ***InterpolationType*** As [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SegmentIndex | Long | Input index value of the segment to set the interpolation information for. This must be a value of 1 to PointCount-1. |
| InterpolationType | [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md) | The type of interpolation to use for this curve segment. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Additional information used to define the shape of the segment for certain interpolation types. |

## Version

Introduced in version 2013
