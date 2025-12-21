# AutoCAD block definitions import

## Description

This sample demonstrates importing AutoCAD block definitions from an external dwg file.

## Code Samples

* [VBA](#VBA)

```
Sub ImportAutoCADBlockDefinitionsFromFile()
    ' Set a reference to the drawing document.
    ' This assumes an Inventor dwg drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Create an array of names of the definitions to import
    Dim oDefNames(1) As String
    oDefNames(0) = "DatumFilled45"
    oDefNames(1) = "Borders Default Border"

    ' Import definitions from an external dwg file
    ' Only the specified definitions will be imported. If you want all definitions
    ' to be imported, you can leave the 2nd argument as unspecified.
    Dim oBlockDefs As AutoCADBlockDefinitionsEnumerator
    Set oBlockDefs = oDrawDoc.AutoCADBlockDefinitions.AddFromFile("C:\temp\acad.dwg", oDefNames)
End Sub
```
