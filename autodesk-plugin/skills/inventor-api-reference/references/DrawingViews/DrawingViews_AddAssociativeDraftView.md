# DrawingViews.AddAssociativeDraftView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a new associative draft . An empty draft view is created and associated with the input document. The newly created DrawingView is returned.

## Syntax

DrawingViews.**AddAssociativeDraftView**( ***Model*** As [Document](../Document/Document.md), ***Position*** As [Point2d](../Point2d/Point2d.md), [***Scale***] As Double, [***Name***] As String ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Model | [Document](../Document/Document.md) | Input Document that specifies the document to associate with this view. Valid document types include part file, assembly files, and presentation files. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| Scale | Double | Optional input Double that specifies the drawing view scale factor. If not specified, a default value of 1.0 is used. |
| Name | String | Optional input String that defines the editable portion of the name that is displayed within the browser.   This is an optional argument whose default value is "". |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |