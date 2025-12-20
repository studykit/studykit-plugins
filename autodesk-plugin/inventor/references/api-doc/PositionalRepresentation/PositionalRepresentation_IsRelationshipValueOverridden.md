# PositionalRepresentation.IsRelationshipValueOverridden Method

Parent Object: [PositionalRepresentation](../PositionalRepresentation/PositionalRepresentation.md)

## Description

Function that returns whether the value of the input assembly relationship is overridden for the positional representation. It also returns the values expression.

## Syntax

PositionalRepresentation.**IsRelationshipValueOverridden**( ***Relationship*** As Object, ***RelationShipValueType*** As [RelationshipValueTypeEnum](../RelationshipValueTypeEnum.md), ***Expression*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Relationship | Object | Input assembly constraint or connection object to be queried for the override. |
| RelationShipValueType | [RelationshipValueTypeEnum](../RelationshipValueTypeEnum.md) | Input RelationshipValueTypeEnum that specifies the value of the assembly constraint or connection object. |
| Expression | String | Output string that returns the expression of the specified value of the assembly constraint or connection object (whether it is overridden or not). |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |