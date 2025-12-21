# RuledSurfaceFeature.GetSuppressionCondition Method

Parent Object: [RuledSurfaceFeature](../RuledSurfaceFeature/RuledSurfaceFeature.md)

## Description

Method that gets the suppression condition for the feature. The method returns False if no condition has been applied.

## Syntax

RuledSurfaceFeature.**GetSuppressionCondition**( ***Parameter*** As [Parameter](../Parameter/Parameter.md), ***ComparisonType*** As [ComparisonTypeEnum](../ComparisonTypeEnum.md), ***Expression*** As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Parameter | [Parameter](../Parameter/Parameter.md) | Parameter object that specifies the parameter whose value is to be checked for feature suppression. |
| ComparisonType | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | ComparisonTypeEnum that specifies the type of comparison. Valid return types are kEqualToComparison, kNotEqualToComparison, kLessThanComparison, kGreaterThanComparison, kLessThanOrEqualToComparison, kGreaterThanOrEqualToComparison. |
| Expression | Variant | Specifies the expression used for the comparison with the parameter value. This can either be a string or a parameter object. |

## Version

Introduced in version 2016
