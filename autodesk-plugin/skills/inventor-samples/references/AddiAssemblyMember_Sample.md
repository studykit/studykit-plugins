# Adding iAssembly occurrences

## Description

This sample demonstrates adding iAssembly occurrences to an assembly.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)

Before running the sample, make sure that C:\temp\iAssemblyFactory.iam exists and that it is an iAssembly factory.

|  |
| --- |
| Copy Code |

```
Public Sub AddiAssemblyOccurrence()
    ' Open the factory document invisible.
    Dim oFactoryDoc As AssemblyDocument
    Set oFactoryDoc = ThisApplication.Documents.Open("C:\temp\iAssemblyFactory.iam", False)

    ' Set a reference to the component definition.
    Dim oCompDef As AssemblyComponentDefinition
    Set oCompDef = oFactoryDoc.ComponentDefinition

    ' Make sure we have an iAssembly factory.
    If oCompDef.IsiAssemblyFactory = False Then
        MsgBox "Chosen document is not a factory.", vbExclamation
        Exit Sub
    End If

    ' Set a reference to the factory.
    Dim oiAssyFactory As iAssemblyFactory
    Set oiAssyFactory = oCompDef.iAssemblyFactory

    ' Get the number of rows in the factory.
    Dim iNumRows As Integer
    iNumRows = oiAssyFactory.TableRows.Count

    ' Create a new assembly document
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject, , True)

    Dim oOccs As ComponentOccurrences
    Set oOccs = oDoc.ComponentDefinition.Occurrences

    Dim oPos As Matrix
    Set oPos = ThisApplication.TransientGeometry.CreateMatrix

    Dim oStep As Double
    oStep = 0#
    Dim iRow As Long

    ' Add an occurrence for each member in the factory.
    For iRow = 1 To iNumRows

        oStep = oStep + 10

        ' Add a translation along X axis
        oPos.SetTranslation ThisApplication.TransientGeometry.CreateVector(oStep, oStep, 0)

        Dim oOcc As ComponentOccurrence
        Set oOcc = oOccs.AddiAssemblyMember("C:\temp\iAssemblyFactory.iam ", oPos, iRow)
    Next
End Sub
```

Before running the sample, make sure that C:/temp/iAssemblyFactory.iam exists and that it is an iAssembly factory. The first line of the C# sample sets the oApp variable to ThisApplication - this should be appropriately changed.

|  |
| --- |
| Copy Code |

```
public void AddiAssemblyOccurrence()
{
    Application oApp = ThisApplication;

    // Open the factory document invisible.
    AssemblyDocument oFactoryDoc = (AssemblyDocument)oApp.Documents.Open("C:/temp/iAssemblyFactory.iam", false);

    // Set a reference to the component definition.
    AssemblyComponentDefinition oCompDef = oFactoryDoc.ComponentDefinition;

    // Make sure we have an iAssembly factory.
    if(!oCompDef.IsiAssemblyFactory)
    {
        System.Windows.Forms.MessageBox.Show("Chosen document is not a factory.", "Invalid document");
        return;
    }

    // Set a reference to the factory.
    iAssemblyFactory oiAssyFactory = oCompDef.iAssemblyFactory;

    // Get the number of rows in the factory.
    int iNumRows = oiAssyFactory.TableRows.Count;

    // Create a new assembly document
    AssemblyDocument oDoc = (AssemblyDocument)oApp.Documents.Add(DocumentTypeEnum.kAssemblyDocumentObject, "" , true);

    ComponentOccurrences oOccs = oDoc.ComponentDefinition.Occurrences;

    Matrix oPos = oApp.TransientGeometry.CreateMatrix();

    int oStep = 0;
    int iRow;

    // Add an occurrence for each member in the factory.
    for (iRow = 1; iRow <= iNumRows; iRow++)
    {
        oStep = oStep + 10;

        // Add a translation along X axis
        oPos.SetTranslation(oApp.TransientGeometry.CreateVector(oStep, oStep, 0), false);

        ComponentOccurrence oOcc = oOccs.AddiAssemblyMember("C:/temp/iAssemblyFactory.iam ", oPos, iRow, null);
    }

    // Release reference of the invisibly open document
    oFactoryDoc.ReleaseReference();

}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |