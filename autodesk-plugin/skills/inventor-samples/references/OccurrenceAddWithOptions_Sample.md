# Create assembly occurrence with representations

## Description

This sample demonstrates how to create an assembly occurrence by specifying various representations.

## Code Samples

* [VBA](#VBA)

Before running this sample, make sure that the file C:\Temp\Reps.iam exists (or change the path in the sample). The file must contain a model state named MyModelState, a positional representation named MyPositionalRep and a design view representation named MyDesignViewRep.

|  |
| --- |
| Copy Code |

```
Public Sub AddOccurrenceWithRepresentations()
    ' Set a reference to the assembly component definintion.
    ' This assumes an assembly document is open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create a matrix. A new matrix is initialized with an identity matrix.
    Dim oMatrix As Matrix
    Set oMatrix = oTG.CreateMatrix

    ' Create a new NameValueMap object
    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap

    ' Set the representations to use when creating the occurrence.
    Call oOptions.Add("ModelState", "MyModelState")
    Call oOptions.Add("PositionalRepresentation", "MyPositionalRep")
    Call oOptions.Add("DesignViewRepresentation", "MyDesignViewRep")
    Call oOptions.Add("DesignViewAssociative", True)

    ' Add the occurrence.
    Dim oOcc As ComponentOccurrence
    Set oOcc = oAsmCompDef.Occurrences.AddWithOptions("C:\Temp\Reps.iam", oMatrix, oOptions)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |