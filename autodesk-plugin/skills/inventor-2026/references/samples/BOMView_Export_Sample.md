# Exporting the assembly BOM

## Description

This sample demonstrates exporting the Assembly BOM to an external file.

## Code Samples

* [VBA](#VBA)

This sample exports the structured and parts only views of the active assembly document to an Excel file. Other file formats are also supported.

```
Public Sub BOMExport()
    ' Set a reference to the assembly document.
    ' This assumes an assembly document is active.
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to the BOM
    Dim oBOM As BOM
    Set oBOM = oDoc.ComponentDefinition.BOM

    ' Set the structured view to 'all levels'
    oBOM.StructuredViewFirstLevelOnly = False

    ' Make sure that the structured view is enabled.
    oBOM.StructuredViewEnabled = True

    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap
    oOptions.Add "TableName", "My BOMView"
    oOptions.Add "StartingCell", "A1"
    ' You can specify a template for the export.
    'oOptions.Add "Template", "C:\Temp\Template.xlsx"
    oOptions.Add "ExportedColumns", "Item;QTY;REV;Description;Part Number"
    oOptions.Add "AutoFitColumnWidth", True
    oOptions.Add "ApplyCellFormatting", True
    oOptions.Add "ForceCellToText", True

    ' Set a reference to the "Structured" BOMView
    Dim oStructuredBOMView As BOMView
    Set oStructuredBOMView = oBOM.BOMViews.Item("Structured")

    ' Export the BOM view to an Excel file
    oStructuredBOMView.Export "C:\temp\BOM-StructuredAllLevels.xls", kMicrosoftExcelFormat, oOptions

    ' Make sure that the parts only view is enabled.
    oBOM.PartsOnlyViewEnabled = True

    ' Set a reference to the "Parts Only" BOMView
    Dim oPartsOnlyBOMView As BOMView
    Set oPartsOnlyBOMView = oBOM.BOMViews.Item("Parts Only")

    ' Export the BOM view to an Excel file
    oPartsOnlyBOMView.Export "C:\temp\BOM-PartsOnly.xls", kMicrosoftExcelFormat, oOptions
End Sub
```
