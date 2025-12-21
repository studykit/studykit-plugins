# Layer.Copy Method

Parent Object: [Layer](../Layer/Layer.md)

## Description

Method that creates a new local Style object. The newly created style is returned.

## Syntax

Layer.**Copy**( ***Name*** As String ) As [Style](../Style/Style.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name for the new style. This name must be unique with respect to all other styles of a similar type in the document. That is, if a dimension style is being copied, the name must be unique with respect to all the other dimension styles. If it is not unique the method will fail. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |