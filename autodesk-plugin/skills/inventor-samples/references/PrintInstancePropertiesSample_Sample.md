# Print instance properties of all components in an assembly

## Description

This sample demonstrates how to get the instance properties of all components in an assembly.

## Code Samples

* [VBA](#VBA)

This VBA sample demonstrates how to get the instance properties of all components in an assembly.

|  |
| --- |
| Copy Code |

```
Sub PrintInstancePropertiesSample()
    If ThisApplication.ActiveDocument Is Nothing Then
        MsgBox "Please open an assembly document!"
    ElseIf (ThisApplication.ActiveDocument.DocumentType <> kAssemblyDocumentObject) Then
        MsgBox "Please open an assembly document!"
    Else

        Dim oDoc As AssemblyDocument
        Set oDoc = ThisApplication.ActiveDocument

        GetInstancePropInfo oDoc.ComponentDefinition.Occurrences

    End If
End Sub

Sub GetInstancePropInfo(oOccus As ComponentOccurrences)

    Dim oOccu As ComponentOccurrence
    Dim oTempOccu As ComponentOccurrence

    ' The Instance Properties is accessiable via ComponentOccurrence only
    ' so below will get the ComponentOccurrence from ComponentOccurrenceProxy.
    For Each oTempOccu In oOccus
        If oTempOccu.Type = kComponentOccurrenceProxyObject Then
            Set oOccu = oTempOccu.NativeObject

        Else
            Set oOccu = oTempOccu
        End If

        Debug.Print oOccu.Name
        '  Instance Properties
        If oOccu.OccurrencePropertySetsEnabled Then
            Dim oProp As Inventor.Property
            For Each oProp In oOccu.OccurrencePropertySets(1)

                ' Print property info
                Debug.Print "    " & oProp.DisplayName & ":" & oProp.Expression
            Next
        End If

        GetInstancePropInfo oTempOccu.SubOccurrences
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |