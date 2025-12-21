# Move DrawingViewAnnotation Text Position Sample

## Description

This sample demonstrates how to move the text position of drawing view annotation. Create a detail or section view before running this sample.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to move the text position of drawing view annotation. Create a detail or section view before running this sample.

```
Sub MoveViewAnnotationTextPositionSample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oView As DrawingView
    Dim oTemp As DrawingView
    For Each oTemp In oDoc.ActiveSheet.DrawingViews
        If oTemp.ViewType = kDetailDrawingViewType Or oTemp.ViewType = kSectionDrawingViewType Then
            Set oView = oTemp

            Dim oViewAnnotation As DrawingViewAnnotation
            Set oViewAnnotation = oView.ViewAnnotation

            ' move the annotation text
            Dim oPt As Point2d
            Set oPt = oViewAnnotation.TextPosition
            oPt.X = oPt.X + 2: oPt.Y = oPt.Y + 3
            oViewAnnotation.TextPosition = oPt

            oDoc.Update
        End If
    Next
End Sub
```

This sample demonstrates how to move the text position of drawing view annotation. Create a detail or section view before running this sample.

```
Sub MoveViewAnnotationTextPositionSample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oView As DrawingView
    Dim oTemp As DrawingView
    For Each oTemp In oDoc.ActiveSheet.DrawingViews
        If oTemp.ViewType = kDetailDrawingViewType Or oTemp.ViewType = kSectionDrawingViewType Then
            Set oView = oTemp

            Dim oViewAnnotation As DrawingViewAnnotation
            Set oViewAnnotation = oView.ViewAnnotation

            ' move the annotation text
            Dim oPt As Point2d
            Set oPt = oViewAnnotation.TextPosition
            oPt.X = oPt.X + 2: oPt.Y = oPt.Y + 3
            oViewAnnotation.TextPosition = oPt

            oDoc.Update
        End If
    Next
End Sub
```
