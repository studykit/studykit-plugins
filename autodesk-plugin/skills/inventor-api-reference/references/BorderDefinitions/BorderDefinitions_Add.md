# BorderDefinitions.Add Method

Parent Object: [BorderDefinitions](../BorderDefinitions/BorderDefinitions.md)

## Description

Method that creates a new border definition. The new BorderDefinition object is returned. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active.

## Syntax

BorderDefinitions.**Add**( ***Name*** As String ) As [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that defines the name of the new border definition. The name specified must be unique with respect to the other border definitions in the document. If a unique name is not specified, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |

## Version

Introduced in version 5.3
