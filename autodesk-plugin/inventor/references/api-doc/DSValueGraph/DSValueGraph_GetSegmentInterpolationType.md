# DSValueGraph.GetSegmentInterpolationType Method

Parent Object: [DSValueGraph](../DSValueGraph/DSValueGraph.md)

## Description

Method that returns the interpolation method used for the specified curve segment. A curve segment is defined as the curve between two of the value points. There are PointCount-1 segments.

## Syntax

DSValueGraph.**GetSegmentInterpolationType**( ***SegmentIndex*** As Long, ***InterpolationType*** As [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SegmentIndex | Long | Input index value of the segment to get the interpolation information for. This must be a value of 1 to PointCount-1. |
| InterpolationType | [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md) | The type of interpolation used for this curve segment. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Additional information used to define the shape of the segment for certain interpolation types. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |