# Aligning drawing dimensions

## Description

This sample demonstrates aligning the selected drawing dimensions along a horizontal or vertical axis.

## Code Samples

* [VBA](#VBA)

The first dimension selected defines the origin of the axis. A drawing document must be open and at least two dimensions selected.

```
Public Sub DimensionAlign()
   Dim oDrawDoc As DrawingDocument
   Set oDrawDoc = ThisApplication.ActiveDocument

   ' Determine if there are any dimensions in the select set.
   Dim oSelectSet As SelectSet
   Set oSelectSet = oDrawDoc.SelectSet
   Dim colDimensions As New Collection
   Dim i As Long
   For i = 1 To oSelectSet.Count
      If Typeof oSelectSet.Item(i) Is DrawingDimension Then
         ' Add any dimensions to the collection. We need to save them
         ' in something besides the selection set because once we start
         ' manipulating them the select set will be cleared.
         colDimensions.Add oSelectSet.Item(i)
      End If
   Next

   If colDimensions.Count < 2 Then
      MsgBox "You must select at least 2 dimensions for this operation."
      Exit Sub
   End If

   ' Ask the user if he/she wants vertical or horizontal alignment.
   Dim bHorizontal As Boolean
   If MsgBox("Do you want horizontal alignment? (Selecting ""No"" results in vertical alignment)", vbQuestion + vbYesNo, "Align Dimensions") = vbYes Then
       bHorizontal = True
   Else
    bHorizontal = False
   End If

   For i = 1 To colDimensions.Count
      Dim oDimension As DrawingDimension
      Set oDimension = colDimensions.Item(i)

      If i = 1 Then
         ' Get the position of the first dimension text. This is
         ' the position the other dimensions will be aligned to.
         Dim dPosition As Double
         If bHorizontal Then
            dPosition = oDimension.Text.Origin.Y
         Else
            dPosition = oDimension.Text.Origin.X
         End If
      Else
         ' Change the position of the dimension.
         Dim oPosition As Point2d
         Set oPosition = oDimension.Text.Origin
         If bHorizontal Then
            oPosition.Y = dPosition
         Else
            oPosition.X = dPosition
         End If

         oDimension.Text.Origin = oPosition
      End If
   Next
End Sub
```
