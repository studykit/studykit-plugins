# DrawingViews.AddDraftView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a new draft . The newly created DrawingView is returned.

## Syntax

DrawingViews.**AddDraftView**( [***Scale***] As Double, [***Name***] As String ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Scale | Double | Optional input Double that specifies the drawing view scale factor. If not specified, a default value of 1.0 is used. |
| Name | String | Optional input String that defines the editable portion of the drawing view name that is displayed within the browser.   This is an optional argument whose default value is "". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drawing Sketches - editing line type and color](../../sample-programs/DrawingSketch_Sample.md) | This sample demonstrates the modification of sketch entity line type and color in drawings. |
| [Draft Views - create](../../sample-programs/DrawingViews_AddDraftView_Sample.md) | This sample demonstrates the creation of a draft view in a drawing. |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |

## Version

Introduced in version 9
