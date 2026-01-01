# LoftSectionDimensions.AddDrivenSection Method

Parent Object: [LoftSectionDimensions](../LoftSectionDimensions/LoftSectionDimensions.md)

## Description

Method that creates a new LoftSectionDimension that represents a driven placed section for an area-graph type loft feature.

## Syntax

LoftSectionDimensions.**AddDrivenSection**( ***Position*** As Double, [***PositionAsAbsoluteDistance***] As Boolean ) As [LoftSectionDimension](../LoftSectionDimension/LoftSectionDimension.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | Double | Specifies the positional distance (from the starting section) of the placed section for an area-graph type loft feature. The valid range of values for this argument depends on the value of the PositionAsAbsoluteDistance argument. If the PositionAsAbsoluteDistance argument is True, then the value specified by this argument represents an absolute distance value (measured along the centerline of the loft from the starting section) and any Double value that represents this absolute distance can be specified. If the PositionAsAbsoluteDistance argument is False, then the value specified by this argument represents a proportional distance value (relative to the starting section). The valid range of values for the proportional distance is 0.0 to 1.0 (including 0.0 and 1.0). This proportional distance is defined as the absolute distance of the placed section from the starting section divided by the absolute distance of the ending section from the starting section where both the distances are measured along the centerline of the loft. For example, for a placed section that coincides with the starting section the value of the proportional distance will be 0.0 and for a placed section that coincides with the ending section the value of the proportional distance will be 1.0. For intermediate placed sections, the value of the proportional distance will be between 0.0 and 1.0. |
| PositionAsAbsoluteDistance | Boolean | Indicates whether the positional distance of the placed section for an area-graph type loft feature is specified as an absolute distance value. A value of True indicates that the positional distance (specified by the Position argument) of the placed section is specified as an absolute distance value (measured along the centerline of the loft from the starting section). A value of False indicates that the positional distance (specified by the Position argument) of the placed section is specified as a proportional distance value (relative to the starting section). This proportional distance is defined as the absolute distance of the placed section from the starting section divided by the absolute distance of the ending section from the starting section where both the distances are measured along the centerline of the loft. For example, for a placed section that coincides with the starting section the value of the proportional distance will be 0.0 and for a placed section that coincides with the ending section the value of the proportional distance will be 1.0. For intermediate placed sections, the value of the proportional distance will be between 0.0 and 1.0. If no value is explicitly specified, a default value of False will be assumed to indicate that positional distance is specified as a proportional distance value. |

## Version

Introduced in version 2008
