# SectionDrawingView.SetActiveModelState Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that sets the active model state for a drawing view. In this method users can also decide to update the PartsList objects which use the same model state as the drawing view. This method fails for drawing views where the model is unresolved.

## Syntax

SectionDrawingView.**SetActiveModelState**( ***ModelState*** As String, [***UpdatePartsList***] As Boolean, [***KeepOverrides***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelState | String | Input String value that specifies the name of active model state to set for the drawing view. |
| UpdatePartsList | Boolean | Optional input Boolean that specifies whether the PartsList objects in the document with the same model state as the drawing view should be updated or not. |
| KeepOverrides | Boolean | Optional input Boolean that specifies whether to keep the overrides in the PartsList objects. This is ignored if the UpdatePartsLists is set to False.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2022
