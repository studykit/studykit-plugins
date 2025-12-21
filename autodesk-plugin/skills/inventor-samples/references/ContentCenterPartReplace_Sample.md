# Replace content center part

## Description

This sample demonstrates how to replace the content part referenced by an assembly occurrence.

## Code Samples

* [VBA](#VBA)

Open an assembly that contains an occurrence of a content part and run the macro.

```
Sub ReplaceContentCenterPart()
    ' Set a reference to the active assembly document.
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Prompt user to pick an occurrence
    Dim oOcc As ComponentOccurrence
    Set oOcc = ThisApplication.CommandManager.Pick(kAssemblyOccurrenceFilter, "Pick occurrence to replace")

    If oOcc.DefinitionDocumentType <> kPartDocumentObject Then
        MsgBox "Occurrence does not reference a content part."
        Exit Sub
    End If

    Dim oOccDef As PartComponentDefinition
    Set oOccDef = oOcc.Definition

    If Not oOccDef.IsContentMember Then
        MsgBox "The occurrence does not reference a content part."
        Exit Sub
    End If

    ' Set a reference to the ContentCenter object.
    Dim oContentCenter As ContentCenter
    Set oContentCenter = ThisApplication.ContentCenter

    ' Get the content node (category) "Fasteners:Bolts:Hex Head"
    Dim oContentNode As ContentTreeViewNode
    Set oContentNode = oContentCenter.TreeViewTopNode.ChildNodes.Item("Fasteners").ChildNodes.Item("Bolts").ChildNodes.Item("Hex Head")

    ' Get the "ISO 4015" Family object.
    Dim oFamily As ContentFamily
    For Each oFamily In oContentNode.Families
        If oFamily.DisplayName = "ISO 4015" Then
            Exit For
        End If
    Next

    ' Create a member based on the second row of the family.
    Dim error As MemberManagerErrorsEnum
    Dim strContentPartFileName As String
    Dim strErrorMessage As String
    strContentPartFileName = oFamily.CreateMember(2, error, strErrorMessage)

    Call oOcc.Replace(strContentPartFileName, False)
End Sub
```
