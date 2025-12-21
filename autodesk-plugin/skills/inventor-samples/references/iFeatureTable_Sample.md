# Place table driven iFeature

## Description

This program demonstrates the placement of a table driven iFeature in a part.

## Code Samples

* [VBA](#VBA)

A part must be open and a planar face on that part selected. There aren't any table driven .ide files delivered with Inventor so one must be constructed to be used as input. The primary assumption this sample makes about the .ide file is that a custom row has been created named 'Size' and one of the rows in this column has the value '4.5.'

```
Public Sub PlaceTableDriveniFeature()
    ' Get the part document and component definition of the active document.
    On Error Resume Next
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    If Err Then
        MsgBox "A part must be active."
        Exit Sub
    End If

    Dim oPartDef As PartComponentDefinition
    Set oPartDef = oPartDoc.ComponentDefinition

    ' Get the selected face to use as input for the iFeature.
    Dim oFace As Face
    Set oFace = oPartDoc.SelectSet.Item(1)
    If Err Then
        MsgBox "A planar face must be selected."
        Exit Sub
    End If
    On Error GoTo 0

    If oFace.SurfaceType  kPlaneSurface Then
        MsgBox "A planar face must be selected."
        Exit Sub
    End If

    Dim oFeatures As PartFeatures
    Set oFeatures = oPartDef.Features

    ' Create an iFeatureDefinition object.
    Dim oiFeatureDef As iFeatureDefinition
    Set oiFeatureDef = oFeatures.iFeatures.CreateiFeatureDefinition( _
"C:\Program Files\Autodesk\Inventor 2010\Catalog\Table\Test.ide")

    ' Set the input, which in this case is only the sketch plane
    ' since the other input comes from the table.  The parameter input
    ' should not be available at this point since it can't be changed
    ' and is controlled by the table.
    '
    ' When an existing table driven iFeature is accessed then this should
    ' include the parameters so the programmer has access to the corresponding
    ' reference parameter that's created.
    Dim bFoundPlaneInput As Boolean
    bFoundPlaneInput = False
    Dim oInput As iFeatureInput
    For Each oInput In oiFeatureDef.iFeatureInputs
        Dim oParamInput As iFeatureParameterInput
        Select Case oInput.Name
            Case "Profile Plane1"
                Dim oPlaneInput As iFeatureSketchPlaneInput
                Set oPlaneInput = oInput
                oPlaneInput.PlaneInput = oFace
                bFoundPlaneInput = True
        End Select
    Next

    If Not bFoundPlaneInput Then
        MsgBox "The ide file does not contain an iFeature input named ""Profile Plane1""."
        Exit Sub
    End If

    '** Look through the table to find the row where "Size" is "4.5".
    Dim oTable As iFeatureTable
    Set oTable = oiFeatureDef.iFeatureTable

    ' Find the "Size" column.
    Dim oColumn As iFeatureTableColumn
    Dim bFoundSize As Boolean
    bFoundSize = False
    For Each oColumn In oTable.iFeatureTableColumns
        If oColumn.DisplayHeading = "Size" Then
            bFoundSize = True
            Exit For
        End If
    Next

    If Not bFoundSize Then
        MsgBox "The column ""Size"" was not found."
        Exit Sub
    End If

    ' Find the row in the "Size" column with the value of "4.5"
    Dim oCell As iFeatureTableCell
    bFoundSize = False
    For Each oCell In oColumn
        If oCell.Value = "4.5" Then
            bFoundSize = True
            Exit For
        End If
    Next

    If Not bFoundSize Then
        MsgBox "The cell with value ""4.5"" was not found."
        Exit Sub
    End If

    ' Set this row as the active row.
    oiFeatureDef.ActiveTableRow = oCell.Row

    ' Create the iFeature.
    Dim oiFeature As iFeature
    Set oiFeature = oFeatures.iFeatures.Add(oiFeatureDef)
End Sub
```
