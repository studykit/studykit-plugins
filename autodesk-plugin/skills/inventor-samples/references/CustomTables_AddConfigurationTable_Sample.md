# Create a Configuration Table

## Description

This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document.

## Code Samples

* [VBA](#VBA)

Change the location of the source part in the code below before running the sample.

```
Public Sub CreateConfigurationTable()
    ' Set a reference to the active drawing document
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Create the placement point for the table
    Dim oPoint As Point2d
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

    ' Open the factory document invisible
    Dim oiPartDoc As PartDocument
    Set oiPartDoc = ThisApplication.Documents.Open("C:\Temp\iPartFactory.ipt", False)

    Dim oiPartFactory As iPartFactory
    Set oiPartFactory = oiPartDoc.ComponentDefinition.iPartFactory

    ' Specify the columns - this sample includes all columns from the factory table
    Dim strColumns() As String
    Redim strColumns(oiPartFactory.TableColumns.Count - 1)

    Dim i As Long
    For i = 1 To oiPartFactory.TableColumns.Count
        strColumns(i - 1) = oiPartFactory.TableColumns.Item(i).Heading
    Next

    ' Release reference on factory document since we opened it invisible
    oiPartDoc.ReleaseReference

    ' Create the configuration table by specifying the source iPart/iAssembly file
    Dim oConfigTable As CustomTable
    Set oConfigTable = oActiveSheet.CustomTables.AddConfigurationTable("C:\Temp\iPartFactory.ipt", oPoint, "Configuration Table", strColumns)
End Sub
```
