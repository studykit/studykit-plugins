# iFeatureParameterInput.LimitType Property

Parent Object: [iFeatureParameterInput](../iFeatureParameterInput/iFeatureParameterInput.md)

## Description

Property that returns the limit type of the parameter. If this returns kParamLimitRange, the LimitExpression property will return the upper and lower limits will be two limit values: the value of the lower and upper bounds. If the LimitType property is kParamLimitList there will be n values. This property will fail in the case where the iFeatureDefinition object is associated with an iFeature instance.

## Syntax

iFeatureParameterInput.**LimitType**() As [iFeatureParamLimitTypeEnum](../iFeatureParamLimitTypeEnum.md)

## Property Value

This is a read only property whose value is an [iFeatureParamLimitTypeEnum](../iFeatureParamLimitTypeEnum.md).

## Version

Introduced in version 6
