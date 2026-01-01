# BaselineDimensionSet.AddMember Method

Parent Object: [BaselineDimensionSet](../BaselineDimensionSet/BaselineDimensionSet.md)

## Description

Method that adds a member to the baseline set and returns a LinearGeneralDimension object. If an existing LinearGeneralDimension is input into the method, the same object is returned.

## Syntax

BaselineDimensionSet.**AddMember**( ***DimensionOrGeometry*** As Object ) As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DimensionOrGeometry | Object | Input object that specifies the member. This can either be an existing LinearGeneralDimension object or a GeometryIntent object that specifies the geometry to dimension to. |

## Version

Introduced in version 2010
