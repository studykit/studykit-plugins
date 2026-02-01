# CircularPatternFeature.SetSuppressionCondition Method

Parent Object: [CircularPatternFeature](../CircularPatternFeature/CircularPatternFeature.md)

## Description

Method that sets the suppression condition for the feature.

## Syntax

CircularPatternFeature.**SetSuppressionCondition**( ***Parameter*** As [Parameter](../Parameter/Parameter.md), ***ComparisonType*** As [ComparisonTypeEnum](../ComparisonTypeEnum.md), ***Expression*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Parameter | [Parameter](../Parameter/Parameter.md) | Parameter object that specifies the parameter whose value is to be checked for feature suppression. |
| ComparisonType | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | ComparisonTypeEnum that specifies the type of comparison. Valid types are kEqualToComparison, kNotEqualToComparison, kLessThanComparison, kGreaterThanComparison, kLessThanOrEqualToComparison, kGreaterThanOrEqualToComparison. |
| Expression | Variant | Specifies the expression used for the comparison with the parameter value. This can either be a string, a value or a parameter object. If a value is input, the database units for the units defined by the parameter are used. For instance, if the parameter defines length units, the value is assumed to be in centimeters. If a string is input, the units can be specified as part of the string or it will default to the current units of the document. For instance, if the parameter defines length units, the current length units of the document are used. |

## Version

Introduced in version 11
