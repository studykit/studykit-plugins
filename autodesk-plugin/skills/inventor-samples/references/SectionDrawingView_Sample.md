# Break alignment of a section view

## Description

Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command.

## Code Samples

* [VBA](#VBA)

```
Sub BreakAlignment()
   Dim oDoc As DrawingDocument
   Set oDoc = ThisApplication.ActiveDocument

   Dim oSectionView As SectionDrawingView
   Set oSectionView = oDoc.ActiveSheet.DrawingViews(2)

   oDoc.SelectSet.Clear
   oDoc.SelectSet.Select oSectionView

   Dim oCtrlDef As ControlDefinition
   Set oCtrlDef = ThisApplication.CommandManager.ControlDefinitions.Item("DrawingBreakViewAlignmentCmd")

   oCtrlDef.Execute

   oDoc.SelectSet.Clear
End Sub
```
