# ModelState.CopyComponentSuppressionToVisibility Method

Parent Object: [ModelState](../ModelState/ModelState.md)

## Description

Method that creates a new design view representation based on the suppression of components as defined by this model state. The newly created DesignViewRepresentation is returned.

## Syntax

ModelState.**CopyComponentSuppressionToVisibility**( [***NewName***] As String ) As [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NewName | String | Optional input string that specifies the name of the design view representation to create. If not specified, Inventor assigns a name to the design view representation. If specified, the name must be unique with respect to the other design view representations in the document |

## Version

Introduced in version 2022
