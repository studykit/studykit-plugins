# EdgeSymbols.CreateDefinition Method

Parent Object: [EdgeSymbols](../EdgeSymbols/EdgeSymbols.md)

## Description

Method that creates a new edge symbol definition.

## Syntax

EdgeSymbols.**CreateDefinition**( [***ValuePositionType***] As Variant, [***IndicationType***] As Variant, [***SymbolOptions***] As Variant ) As [EdgeSymbolDefinition](../EdgeSymbolDefinition/EdgeSymbolDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ValuePositionType | Variant | Optional input EdgeSymbolValuePositionTypeEnum  indicating the text position type of the edge symbol. If not provided, this defaults to kEdgeSymbolValueDirectionVertical. |
| IndicationType | Variant | Optional input EdgeSymbolIndicationTypeEnum  indicating the indication type. If not provided, this defaults to kAllEdgesIndicationType.   This is an optional argument whose default value is null. |
| SymbolOptions | Variant | Optional input NameValueMap to specify more options for the definition. Below are the options can be specified: Name = RangeOfValues. Value = Boolean indicating if use the range of values. If not provided, this defaults to False. Name = StatesOfAllEdgesAroundProfile. Value = Boolean indicating the states of all edges around the profile of a part. If not provided, this defaults to False. Name = SidesDefined. Value = Boolean indicating the states of all edges around the profile of a part with sides clearly defined. If not provided, this defaults to False. Name = ReferenceToISO. Value = Boolean indicating whether to reference to ISO 13715. If not provided, this defaults to False. Name = VerticalValue. Value = String value indicating the vertical value. This is applicable when the ValuePositionType is set to kEdgeSymbolValueVerticalDirectionDefined or kEdgeSymbolValueVerticalAndHorizontalDirectionDefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = VerticalValueLower. Value = String value indicating the vertical value lower. This is applicable when the RangeOfValues is set to True and ValuePositionType is set to kEdgeSymbolValueVerticalDirectionDefined or kEdgeSymbolValueVerticalAndHorizontalDirectionDefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = HorizontalValue. Value = String value indicating the horizontal value. This is applicable when the ValuePositionType is set to kEdgeSymbolValueHorizontalDirectionDefined or kEdgeSymbolValueVerticalAndHorizontalDirectionDefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = HorizontalValueLower. Value = String value indicating the horizontal value lower. This is applicable when the RangeOfValues is set to True and the ValuePositionType is set to kEdgeSymbolValueHorizontalDirectionDefined or kEdgeSymbolValueVerticalAndHorizontalDirectionDefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = UndefinedValue. Value = String value indicating the direction undefined value. This is applicable when the ValuePositionType is set to kEdgeSymbolValueDirectionUndefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = UndefinedValueLower. Value = String value indicating the direction undefined value lower. This is applicable when the RangeOfValues is set to True and ValuePositionType is set to kEdgeSymbolValueDirectionUndefined. The value should contain at least a sign “+”, “-” or “±”, and if “±” is specified a number should be specified along with it. Name = Edges. Value = String value indicating the edges text. This is applicable when the SidesDefined is set to True.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [EdgeSymbol Creation Sample](../../sample-programs/EdgeSymbolCreation_Sample.md) | This sample is to demonstrate how to create a EdgeSymbol in drawing document. |

## Version

Introduced in version 2024
