# DrawingBOMs.IsDrawingBOMDefined Method

Parent Object: [DrawingBOMs](../DrawingBOMs/DrawingBOMs.md)

## Description

Method that returns whether BOM properties have been defined in the drawing for the input model.

## Remarks

If the method returns False, it indicates that no balloons or parts lists have been created in the drawing document based on the input model. If the method returns True, balloons and/or parts list have been created based on the model and the various BOM properties and numbering schemes should not be specified when creating additional balloons or parts lists.

## Syntax

DrawingBOMs.**IsDrawingBOMDefined**( ***FullFileName*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies a model document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |

## Version

Introduced in version 2009
