# CentermarkStyle.Copy Method

Parent Object: [CentermarkStyle](../CentermarkStyle/CentermarkStyle.md)

## Description

Method that creates a new local Style object. The newly created style is returned.

## Syntax

CentermarkStyle.**Copy**( ***Name*** As String ) As [Style](../Style/Style.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name for the new style. This name must be unique with respect to all other styles of a similar type in the document. That is, if a dimension style is being copied, the name must be unique with respect to all the other dimension styles. If it is not unique the method will fail. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |