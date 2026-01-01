# AttributeSet.Add Method

Parent Object: [AttributeSet](../AttributeSet/AttributeSet.md)

## Description

Method that creates a new attribute in the attribute set. The created Attribute object is returned.

## Syntax

AttributeSet.**Add**( ***AttributeName*** As String, ***ValueType*** As [ValueTypeEnum](../ValueTypeEnum.md), ***Value*** As Variant ) As [Attribute](../Attribute/Attribute.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeName | String | Input String value that specifies the name of the attribute. The name must be unique with respect to the other attributes within this attribute set. If it is not unique, a failure will occur. A failure will also occur if the name contains a space. |
| ValueType | [ValueTypeEnum](../ValueTypeEnum.md) | Input value from that specifies the type of the attribute. |
| Value | Variant | Input Variant value that specifies the value of the attribute. |

## Version

Introduced in version 5
