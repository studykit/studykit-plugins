# Assembly Add Occurrence

## Description

This sample demonstrates placing an assembly occurrence.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)

Before running the sample, you need to open an assembly and create a part file called C:\Temp\Part1.ipt, or edit the sample code to point to another part file if desired.

|  |
| --- |
| Copy Code |

```
Public Sub AddOccurrence()
    ' Set a reference to the assembly component definintion.
    ' This assumes an assembly document is open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create a matrix.  A new matrix is initialized with an identity matrix.
    Dim oMatrix As Matrix
    Set oMatrix = oTG.CreateMatrix

    ' Set the rotation of the matrix for a 45 degree rotation about the Z axis.
    Call oMatrix.SetToRotation(3.14159265358979 / 4, _
                            oTG.CreateVector(0, 0, 1), oTG.CreatePoint(0, 0, 0))

    ' Set the translation portion of the matrix so the part will be positioned
    ' at (3,2,1).
    Call oMatrix.SetTranslation(oTG.CreateVector(3, 2, 1))

    ' Add the occurrence.
    Dim oOcc As ComponentOccurrence
    Set oOcc = oAsmCompDef.Occurrences.Add("C:\Temp\Part1.ipt", oMatrix)
End Sub
```

Before running the sample, you need to open an assembly and create a part file called C:/Temp/Part1.ipt, or edit the sample code to point to another part file if desired. The first line of the C# sample sets the oApp variable to ThisApplication - this should be appropriately changed.

|  |
| --- |
| Copy Code |

```
public void AddOccurrence()
{
    Application oApp = ThisApplication;

    // Set a reference to the active assembly document.
    // This assumes an assembly document is open.
    AssemblyDocument oDoc = (AssemblyDocument)oApp.ActiveDocument;

    // Set a reference to the assembly component definition.
    AssemblyComponentDefinition oAsmCompDef = oDoc.ComponentDefinition;

    // Set a reference to the transient geometry object.
    TransientGeometry oTG = oApp.TransientGeometry;

    // Create a matrix.  A new matrix is initialized with an identity matrix.
    Matrix oMatrix = oTG.CreateMatrix();

    // Set the rotation of the matrix for a 45 degree rotation about the Z axis.
    oMatrix.SetToRotation(3.14159265358979 / 4,
        oTG.CreateVector(0, 0, 1), oTG.CreatePoint(0, 0, 0));

    // Set the translation portion of the matrix so the part will be positioned
    // at (3,2,1).
    oMatrix.SetTranslation(oTG.CreateVector(3, 2, 1), true);

    // Add the occurrence.
    ComponentOccurrence oOcc = oAsmCompDef.Occurrences.Add("C:/Temp/Part1.ipt", oMatrix);

}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |