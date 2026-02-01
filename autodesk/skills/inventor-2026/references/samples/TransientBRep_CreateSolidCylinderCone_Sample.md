# Client graphics creation of 3D primitives

## Description

This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)

To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics.

```
Public Sub ClientGraphics3DPrimitives()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    ' Set a reference to component definition of the active document.
    ' This assumes that a part or assembly document is active.
    Dim oCompDef As ComponentDefinition
    Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Check to see if the test graphics data object already exists.
    ' If it does clean up by removing all associated of the client graphics
    ' from the document. If it doesn't create it.
    On Error Resume Next
    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Item("Sample3DGraphicsID")
    If Err.Number = 0 Then
        On Error GoTo 0
        ' An existing client graphics object was successfully obtained so clean up.
        oClientGraphics.Delete

        ' update the display to see the results.
        ThisApplication.ActiveView.Update
    Else
        Err.Clear
        On Error GoTo 0

        ' Set a reference to the transient geometry object for user later.
        Dim oTransGeom As TransientGeometry
        Set oTransGeom = ThisApplication.TransientGeometry

        ' Create the ClientGraphics object.
        Set oClientGraphics = oCompDef.ClientGraphicsCollection.Add("Sample3DGraphicsID")

        ' Create a new graphics node within the client graphics objects.
        Dim oSurfacesNode As GraphicsNode
        Set oSurfacesNode = oClientGraphics.AddNode(1)

        Dim oTransientBRep As TransientBRep
        Set oTransientBRep = ThisApplication.TransientBRep

        ' Create a point representing the center of the bottom of the cone
        Dim oBottom As Point
        Set oBottom = ThisApplication.TransientGeometry.CreatePoint(0, 0, 0)

        ' Create a point representing the tip of the cone
        Dim oTop As Point
        Set oTop = ThisApplication.TransientGeometry.CreatePoint(0, 10, 0)

        ' Create a transient cone body
        Dim oBody As SurfaceBody
        Set oBody = oTransientBRep.CreateSolidCylinderCone(oBottom, oTop, 5, 5, 0)

        ' Reset the top point indicating the center of the top of the cylinder
        Set oTop = ThisApplication.TransientGeometry.CreatePoint(0, -40, 0)

        ' Create a transient cylinder body
        Dim oCylBody As SurfaceBody
        Set oCylBody = oTransientBRep.CreateSolidCylinderCone(oBottom, oTop, 2.5, 2.5, 2.5)

        ' Union the cone and cylinder bodies
        Call oTransientBRep.DoBoolean(oBody, oCylBody, kBooleanTypeUnion)

        ' Create client graphics based on the transient body
        Dim oSurfaceGraphics As SurfaceGraphics
        Set oSurfaceGraphics = oSurfacesNode.AddSurfaceGraphics(oBody)

        ' Update the view to see the resulting curves.
        ThisApplication.ActiveView.Update
    End If
End Sub
```

To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. The first line of this sample sets the oApp variable to ThisApplication - this should be appropriately changed.

```
public void ClientGraphics3DPrimitives()
{
    Application oApp = ThisApplication;
    Document oDoc = oApp.ActiveDocument;

    // Set a reference to component definition of the active document.
    // This assumes that a part or assembly document is active.
    Type t = null;
    if (oDoc.DocumentType == DocumentTypeEnum.kPartDocumentObject)
    {
        t = typeof(PartDocument);
    }
    else if (oDoc.DocumentType == DocumentTypeEnum.kAssemblyDocumentObject)
    {
        t = typeof(AssemblyDocument);
    }

    System.Reflection.PropertyInfo pi = t.GetProperty("ComponentDefinition");
    ComponentDefinition oCompDef = (ComponentDefinition)pi.GetValue(oDoc, null);

    // Check to see if the test graphics data object already exists.
    // If it does clean up by removing all associated of the client graphics
    // from the document. If it doesn't create it.
    ClientGraphics oClientGraphics;
    try
    {
        oClientGraphics = oCompDef.ClientGraphicsCollection["Sample3DGraphicsID"];

        // An existing client graphics object was successfully obtained so clean up.
        oClientGraphics.Delete();

        // update the display to see the results.
        oApp.ActiveView.Update();

    }
    catch
    {
        // Set a reference to the transient geometry object for user later.
        TransientGeometry oTransGeom = oApp.TransientGeometry;

        // Create the ClientGraphics object.
        oClientGraphics = oCompDef.ClientGraphicsCollection.Add("Sample3DGraphicsID");

        // Create a new graphics node within the client graphics objects.
        GraphicsNode oSurfacesNode = oClientGraphics.AddNode(1);

        TransientBRep oTransientBRep = oApp.TransientBRep;

        // Create a point representing the center of the bottom of the cone
        Point oBottom = oApp.TransientGeometry.CreatePoint(0, 0, 0);

        // Create a point representing the tip of the cone
        Point oTop = oApp.TransientGeometry.CreatePoint(0, 10, 0);

        // Create a transient cone body
        SurfaceBody oBody = oTransientBRep.CreateSolidCylinderCone(oBottom, oTop, 5, 5, 0, null);

        // Reset the top point indicating the center of the top of the cylinder
        oTop = oApp.TransientGeometry.CreatePoint(0, -40, 0);

        // Create a transient cylinder body
        SurfaceBody oCylBody = oTransientBRep.CreateSolidCylinderCone(oBottom, oTop, 2.5, 2.5, 2.5, null);

        // Union the cone and cylinder bodies
        oTransientBRep.DoBoolean(oBody, oCylBody, BooleanTypeEnum.kBooleanTypeUnion);

        // Create client graphics based on the transient body
        SurfaceGraphics oSurfaceGraphics = oSurfacesNode.AddSurfaceGraphics(oBody);

        // Update the view to see the resulting curves.
        oApp.ActiveView.Update();
    }
}
```
