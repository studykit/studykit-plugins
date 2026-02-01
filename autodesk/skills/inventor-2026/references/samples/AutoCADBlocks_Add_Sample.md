# AutoCAD block insertion

## Description

Demonstrates inserting an AutoCAD block.

## Code Samples

* [VBA](#VBA)

Open an Inventor dwg file and run the following macro.

```
Public Sub InsertAutoCADBlockOnSheet()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Obtain a reference to the desired AutoCAD block definition.
    Dim oBlockDef As AutoCADBlockDefinition
    Set oBlockDef = oDrawDoc.AutoCADBlockDefinitions.Item("Filled-1")

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' If the definition contains prompted string inputs...
    'Dim sPromptStrings(1) As String
    'sPromptStrings(0) = "String 1"
    'sPromptStrings(1) = "String 2"

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Add an instance of the block definition to the sheet.
    ' Rotate the instance by 45 degrees and scale by .75 when adding.
    ' The symbol will be inserted at (10,10) on the sheet.
    Dim oAutoCADBlock As AutoCADBlock
    Set oAutoCADBlock = oSheet.AutoCADBlocks.Add(oBlockDef, oTG.CreatePoint2d(10, 10), (3.14159 / 4), 0.75)
End Sub
```
