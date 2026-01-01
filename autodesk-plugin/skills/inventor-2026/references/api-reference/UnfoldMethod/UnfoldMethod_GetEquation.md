# UnfoldMethod.GetEquation Method

Parent Object: [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Description

Method that sets this unfold method to be an equation type of unfold method and defines the associated equation and limits.

## Syntax

UnfoldMethod.**GetEquation**( ***Index*** As Long, ***Equation*** As String, ***MinimumValue*** As String, ***MinimumCompareCondition*** As [ComparisonTypeEnum](../ComparisonTypeEnum.md), ***BoundedVariable*** As String, ***MaximumValue*** As String, ***MaximumCompareCondition*** As [ComparisonTypeEnum](../ComparisonTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that specifies which equation to get. Valid values are 1 to the current value of the UnfoldMethod.EquationCount property. |
| Equation | String | Output String that contains the equation. This String uses xml like syntax to allow the inclusion of predefined variables. The available variables and an example of their use are shown below.  `<Angle\>` - Variable used to specify the bend angle within an equation (β).  `<Thickness\>` - Variable used to specify the thickness within an equation (μ).  `<Radius\>` - Variable used to specify the inner radius within an equation (ρ).  `<Pi\>` - Variable used to specify pi within an equation (π).  **Example:**  `"<Pi\> * ((180 deg - <Angle\>)/180 deg) * (<Radius\> + (<Thickness\>/2 ul) * (0.65 ul + 0.5 ul * log(<Radius\> / <Thickness\>))) – 2 ul * (<Radius\> + <Thickness\> * tan(( 180 deg - <Angle\>) / 2 ul)"` |
| MinimumValue | String | Output String that specifies the minimum value. |
| MinimumCompareCondition | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | Output value that specifies the comparison type used for the minimum value. Valid values are kGreaterThanComparisonType, kGreaterThanOrEqualToComparisonType, and kEqualToComparisonType. |
| BoundedVariable | String | Output String that specifies the name of the variable whose values are being bounded. Possible returned values are "Angle" (β), "Thickness" (μ), and "Radius" (ρ). |
| MaximumValue | String | Output String that specifies the maximum value. If an empty string is returned then no maximum value is defined. |
| MaximumCompareCondition | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | Output value that specifies the comparison type used for the maximum value. If the MaximumValue is an empty string the value of this argument should be ignored. Valid values are kLessThanComparisonType or kLessThanOrEqualToComparisonType. |

## Version

Introduced in version 2010
