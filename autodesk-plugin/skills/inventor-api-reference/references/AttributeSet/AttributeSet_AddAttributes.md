# AttributeSet.AddAttributes Method

Parent Object: [AttributeSet](../AttributeSet/AttributeSet.md)

## Description

Adds attributes to the AttributeSet using the arrays that specify the names, valuetypes and values of the desired attributes

## Syntax

AttributeSet.**AddAttributes**( ***AttributeNames***() As String, ***ValueTypes***() As [ValueTypeEnum](../ValueTypeEnum.md), ***Values***() As Variant, ***ReplaceExisting*** As Boolean ) As [AttributesEnumerator](../AttributesEnumerator/AttributesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeNames | String | String array that specifies the names of the attributes. |
| ValueTypes | [ValueTypeEnum](../ValueTypeEnum.md) | Array of ValueTypeEnums that specify the types of the attributes. |
| Values | Variant | Array of Variant values that specify the values of the attributes. |
| ReplaceExisting | Boolean | Indicates whether to replace any attributes that already exist. |

## Version

Introduced in version 11
