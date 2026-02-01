# Table Parameters

## Description

This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet.

## Code Samples

* [VBA](#VBA)

To run the sample, you need to have a part document open, and the spreadsheet C:\Temp\params.xls must exist. You can also edit the sample to reference another spreadsheet if you prefer. The spreadsheet should contain valid definitions for parameters. For the section of the code that demonstrates changing the reference you also need to create a spreadsheet C:\Temp\newparams.xls, or edit the sample to reference another spreadsheet.

```
Public Sub TableParameters()
    Dim oPartDoc As Inventor.PartDocument
    ' Obtain the active document, this assumes that
    ' a part document is active in Inventor
    Set oPartDoc = ThisApplication.ActiveDocument

    'Obtain the Parameters collection
    Dim oParams As Parameters
    Set oParams = oPartDoc.ComponentDefinition.Parameters

    ' Add a parameter table using an existing spreadsheet.
    oParams.ParameterTables.AddExcelTable "C:\Temp\params.xls", "A1", True

    ' Accessing a parameters in a linked/embedded file
    Dim oParamTableFiles As ParameterTables
    Set oParamTableFiles = oParams.ParameterTables

    ' Traverse through the collection of linked files
    Dim oParamTableFile As ParameterTable
    For Each oParamTableFile In oParamTableFiles
        ' Change the linked file to another file
        If LCase(oParamTableFile.FileName) = "C:\temp\params.xls" Then
            oParamTableFile.FileName = "C:\Temp\newparams.xls"
        End If

        ' Get the Parameters collection from the file
        Dim oTableParams As TableParameters
        Set oTableParams = oParamTableFile.TableParameters

        ' Traverse through the table parameters collection and display them
        Dim iNumTableParams As Long
        Debug.Print "TABLE PARAMETER VALUES"
        For iNumTableParams = 1 To oTableParams.Count
            ' Display the name
            Debug.Print " Name: " & oTableParams.Item(iNumTableParams).Name

            ' Display the expression
            Debug.Print " Expression: " & oTableParams.Item(iNumTableParams).Expression

            ' Display the value.  This will be in database units.
            Debug.Print " Value: " & oTableParams.Item(iNumTableParams).Value
        Next iNumTableParams
    Next
End Sub
```
