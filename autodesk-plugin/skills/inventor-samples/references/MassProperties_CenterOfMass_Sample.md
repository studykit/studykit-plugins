# Work point at mass center

## Description

This sample demonstrates creating a fixed work point and edit its position. It does this by computing the the center of mass of the part and creating a work point at that position. Subsequent runs of the sample reposition the work point at the new center of mass.

## Code Samples

* [C#](#C#)
* [VBA](#VBA)

The first line of this sample sets the oApp variable to ThisApplication - this should be appropriately changed.

|  |
| --- |
| Copy Code |

```
public void WorkPointAtMassCenter()
{
    Application oApp = ThisApplication;

    // Check to make sure a part document is active.
    if (oApp.ActiveDocumentType != DocumentTypeEnum.kPartDocumentObject)
    {
        System.Windows.Forms.MessageBox.Show("A part document must be active.", "Part not active");
        return;
    }

    // Set a reference to the active document.
    PartDocument oDoc = (PartDocument)oApp.ActiveDocument;

    // Get the Center of Mass.
    Point oCenterOfMass = oDoc.ComponentDefinition.MassProperties.CenterOfMass;

    // Check to see if a work point for center of mass already exists.
    // This uses the name of the work feature to identify it.

    WorkPoint oWorkPoint = null;
    try
    {
        oWorkPoint = oDoc.ComponentDefinition.WorkPoints["Center Of Mass"];

        FixedWorkPointDef oFixedDef = (FixedWorkPointDef)oWorkPoint.Definition;
        oFixedDef.Point = oCenterOfMass;
        oDoc.Update();
    }
    catch
    {
        // Create a new workpoint at the location of the center of mass.
        oWorkPoint = oDoc.ComponentDefinition.WorkPoints.AddFixed(oCenterOfMass, false);

        // Rename the work point.
        oWorkPoint.Name = "Center Of Mass";
    }
}
```

|  |
| --- |
| Copy Code |

```
Public Sub WorkPointAtMassCenter()
    ' Check to make sure a part document is active.
    If ThisApplication.ActiveDocumentType <> kPartDocumentObject Then
        MsgBox "A part document must be active."
        Exit Sub
    End If

    ' Set a reference to the active document.
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    ' Get the Center of Mass.
    Dim oCenterOfMass As Point
    Set oCenterOfMass = oDoc.ComponentDefinition.MassProperties.CenterOfMass

    ' Check to see if a work point for center of mass already exists.
    ' This uses the name of the work feature to identify it.
    On Error Resume Next
    Dim oWorkPoint As WorkPoint
    Set oWorkPoint = oDoc.ComponentDefinition.WorkPoints.Item("Center Of Mass")
    If Err.Number = 0 Then
        Dim oFixedDef As FixedWorkPointDef
        Set oFixedDef = oWorkPoint.Definition

        oFixedDef.Point = oCenterOfMass
        oDoc.Update
    Else
        ' Create a new workpoint at the location of the center of mass.
        Set oWorkPoint = oDoc.ComponentDefinition.WorkPoints.AddFixed(oCenterOfMass)

        ' Rename the work point.
        oWorkPoint.Name = "Center Of Mass"
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |