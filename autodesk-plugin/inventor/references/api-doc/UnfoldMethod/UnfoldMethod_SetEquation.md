# UnfoldMethod.SetEquation Method

Parent Object: [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Description

Method that creates or edits an equation associated with this unfold method. Creating the first equation will change the unfold method be to a custom equation type of unfold method.

## Syntax

UnfoldMethod.**SetEquation**( ***Index*** As Long, ***EquationType*** As [UnfoldMethodEquationTypeEnum](../UnfoldMethodEquationTypeEnum.md), ***Equation*** As String, [***MinimumValue***] As String, [***MinimumCompareCondition***] As [ComparisonTypeEnum](../ComparisonTypeEnum.md), [***BoundedVariable***] As String, [***MaximumValue***] As String, [***MaximumCompareCondition***] As [ComparisonTypeEnum](../ComparisonTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that specifies which equation to set. When editing an existing equation, valid values are 1 to the current value of the UnfoldMethod.EquationCount property. Any value outside of this range will cause a new equation to be created.  If a new equation is created it will be positioned within the existing equations depending on how its bounding conditions compare to the other equations. This is the same behavior as in the user-interface. |
| EquationType | [UnfoldMethodEquationTypeEnum](../UnfoldMethodEquationTypeEnum.md) | Input value from UnfoldMethodEquationTypeEnum that specifies the type of equation being defined. |
| Equation | String | Inputt String that contains the equation. This String uses xml like syntax to allow the inclusion of predefined variables. The available variables and an example of their use are shown below.  `<Angle\>` - Variable used to specify the bend angle within an equation (β).  `<Thickness\>` - Variable used to specify the thickness within an equation (μ).  `<Radius\>` - Variable used to specify the inner radius within an equation (ρ).  `<Pi\>` - Variable used to specify pi within an equation (π).  **Example:**  `"<Pi\> * ((180 deg - <Angle\>)/180 deg) * (<Radius\> + (<Thickness\>/2 ul) * (0.65 ul + 0.5 ul * log(<Radius\> / <Thickness\>))) – 2 ul * (<Radius\> + <Thickness\> * tan(( 180 deg - <Angle\>) / 2 ul)"` |
| MinimumValue | String | Optional input String that specifies the minimum value. This can be any valid expression. If this argument is supplied the MinimumCompareCondition and BoundedVariable arguments must also be provided. The maximum value is optional. If this is not supplied then there is no minimum limit to the value. |
| MinimumCompareCondition | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | Optional input value from ComparisonTypeEnum that specifies the method used to compare the value to the minimum value. Valid values are kGreaterThanComparisonTypekLessThanComparisonType, kGreaterThanOrEqualToComparisonTypekLessThanOrEqualToComparisonType, or kEqualToComparisonType. If this argument is supplied the MinimumValue and BoundedVariable arguments must also be provided.   This is an optional argument whose default value is 60421. |
| BoundedVariable | String | Optional input String that specifies the name of the variable whose values are being bounded. Possible values are "Angle" (β), "Thickness" (μ), and "Radius" (ρ).   This is an optional argument whose default value is "Angle". |
| MaximumValue | String | Optional input String that specifies the maximum value as an expression. This argument is ignored in the case where the MinimumCompareCondition is kEqualToComparisonType.   This is an optional argument whose default value is "180 deg". |
| MaximumCompareCondition | [ComparisonTypeEnum](../ComparisonTypeEnum.md) | Optional input value from ComparisonTypeEnum that specifies the method used to compare the value to the maximum value. Valid values are kLessThanComparisonType or kLessThanOrEqualToComparisonType. This argument is ignored in the case where the MinimumCompareCondition is kEqualToComparisonType.   This is an optional argument whose default value is 60421. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |