# iFeatureParameterInput.LimitRangeExpressions Method

Parent Object: [iFeatureParameterInput](../iFeatureParameterInput/iFeatureParameterInput.md)

## Description

Method that gets the expressions of the LimitType kParamLimitRange. If the LeftLimitValue and LeftRangeSpec strings are NULL, there is no lower limit for the values that the user can enter. Similarly if the RightLimitValue and RightRangeSpec strings are NULL, there is no upper limit for the values that the user can enter. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance.

## Syntax

iFeatureParameterInput.**LimitRangeExpressions**( ***LeftLimitValue*** As String, ***LeftRangeSpec*** As String, ***RightRangeSpec*** As String, ***RightLimitValue*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeftLimitValue | String | Output String that contains the expression of the lower limit value. If an empty string is returned then there is no lower limit. |
| LeftRangeSpec | String | Output String that contains the comparison operator used for the lower range. If an empty string is returned then there is no lower limit. |
| RightRangeSpec | String | Output String that contains the expression of the upper limit value. If an empty string is returned then there is no upper limit. |
| RightLimitValue | String | Output String that contains the comparison operator used for the upper range. If an empty string is returned then there is no upper limit. |

## Version

Introduced in version 6
