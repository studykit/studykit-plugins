# iFeatureParameterInput Object

Derived from: [iFeatureInput](../iFeatureInput/iFeatureInput.md) Object

## Description

The iFeatureParameterInput object contains the information associated with a parameter of an iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [LimitListExpressions](../iFeatureParameterInput/iFeatureParameterInput_LimitListExpressions.md) | Method that gets the expressions of the LimitType kParamLimitList. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance. |
| [LimitRangeExpressions](../iFeatureParameterInput/iFeatureParameterInput_LimitRangeExpressions.md) | Method that gets the expressions of the LimitType kParamLimitRange. If the LeftLimitValue and LeftRangeSpec strings are NULL, there is no lower limit for the values that the user can enter. Similarly if the RightLimitValue and RightRangeSpec strings are NULL, there is no upper limit for the values that the user can enter. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureParameterInput/iFeatureParameterInput_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DefaultExpression](../iFeatureParameterInput/iFeatureParameterInput_DefaultExpression.md) | Property that gets the expression which specifies the default value and unit. This is the default value of the Expression property. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance. |
| [EntityType](../iFeatureParameterInput/iFeatureParameterInput_EntityType.md) | Property that returns the type of geometry that are valid. The value returned is the sum of values specifying the valid entity types. |
| [Expression](../iFeatureParameterInput/iFeatureParameterInput_Expression.md) | Gets and sets the expression of the parameter. |
| [IsPunchToolDepth](../iFeatureParameterInput/iFeatureParameterInput_IsPunchToolDepth.md) | Property specifies if this parameter input is used to define the custom depth of a punch tool. |
| [LimitListCount](../iFeatureParameterInput/iFeatureParameterInput_LimitListCount.md) | Property that returns the number of limit values if the LimitType is kParamLimitList. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance. |
| [LimitType](../iFeatureParameterInput/iFeatureParameterInput_LimitType.md) | Property that returns the limit type of the parameter. If this returns kParamLimitRange, the LimitExpression property will return the upper and lower limits will be two limit values: the value of the lower and upper bounds. If the LimitType property is kParamLimitList there will be n values. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance. |
| [Name](../iFeatureParameterInput/iFeatureParameterInput_Name.md) | Property that gets the name associated with this input. When placing an iFeature using the API you can use the name to identify each input when assigning the desired values and entities. |
| [Parameter](../iFeatureParameterInput/iFeatureParameterInput_Parameter.md) | Property that returns the parameter in the model this iFeature parameter is dependent on. This property will return Nothing in the case where the iFeatureDefinition object is not associated with an iFeature instance. |
| [Prompt](../iFeatureParameterInput/iFeatureParameterInput_Prompt.md) | Property that gets the prompt that is used for this input during the placement of the iFeature. |
| [Type](../iFeatureParameterInput/iFeatureParameterInput_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../iFeatureParameterInput/iFeatureParameterInput_Value.md) | Gets/(Sets) the evaluation of this iFeature parameter in database units. Setting this is equivalent to setting the 'Expression' with the constant string. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 6
