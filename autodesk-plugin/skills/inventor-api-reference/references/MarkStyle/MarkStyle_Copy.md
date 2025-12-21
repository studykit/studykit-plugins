# MarkStyle.Copy Method

Parent Object: [MarkStyle](../MarkStyle/MarkStyle.md)

## Description

Method that creates a new local style object.

## Syntax

MarkStyle.**Copy**( ***NewName*** As String ) As [MarkStyle](../MarkStyle/MarkStyle.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NewName | String | Input String that specifies the name for the new style. This name must be unique with respect to all other styles of a similar type in the document. That is, if a mark style is being copied, the name must be unique with respect to all the other mark styles. If it is not unique the method will fail. |

## Version

Introduced in version 2023
