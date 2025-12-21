# TitleBlockDefinitions.Add Method

Parent Object: [TitleBlockDefinitions](../TitleBlockDefinitions/TitleBlockDefinitions.md)

## Description

Method that creates a new title block definition. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active.

## Syntax

TitleBlockDefinitions.**Add**( ***Name*** As String ) As [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that defines the name of the new title block definition. The name specified must be unique with respect to the other title block definitions in the document. If a unique name is not specified, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
