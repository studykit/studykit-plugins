# Selection of Surface Graphics Primitives

## Description

This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case).

## Code Samples

* [VBA](#VBA)

To use this sample a part or assembly must be active.

```
Public Sub SelectablePrimitives()
    ' Make sure a part or assembly is active.
    If ThisApplication.ActiveDocumentType <> kAssemblyDocumentObject And ThisApplication.ActiveDocumentType <> kPartDocumentObject Then
        MsgBox "A part or assembly must be active."
        Exit Sub
    End If

    ' Get the document and it's associated definition.
    Dim doc As Document
    Set doc = ThisApplication.ActiveDocument
    Dim def As ComponentDefinition
    Set def = doc.ComponentDefinition

    ' Get an .ipt or SAT filename from the user.
    Dim dialog As FileDialog
    Dim filename As String
    Call ThisApplication.CreateFileDialog(dialog)
    With dialog
        .Filter = "Inventor Part File (*.ipt)|*.ipt|ACIS SAT File (*.sat)|*.sat"
        .FilterIndex = 0
        .ShowOpen
        If .filename = "" Then
            Exit Sub
        Else
            filename = .filename
        End If
    End With

    ' Get the transient B-Rep object.
    Dim tb As TransientBRep
    Set tb = ThisApplication.TransientBRep

    ' If a part was selected, open it inivisibly and get the body.
    Dim body As SurfaceBody
    If UCase(Right$(filename, 4)) = ".IPT" Then
        Dim newPart As PartDocument
        Set newPart = ThisApplication.Documents.Open(filename, False)

        ' Copy out the first body of the part.
        Set body = tb.Copy(newPart.ComponentDefinition.SurfaceBodies.Item(1))
    Else
        ' Read in the sat file.
        Dim bodies As SurfaceBodies
        Set bodies = tb.ReadFromFile(filename)

        Set body = bodies.Item(1)
    End If

    ' Create the client graphics object.
    Dim graphics As ClientGraphics
    On Error Resume Next
    Set graphics = def.ClientGraphicsCollection.Item("Test")
    If Err.Number = 0 Then
        graphics.Delete
    End If
    On Error GoTo 0

    Set graphics = def.ClientGraphicsCollection.Add("Test")
    Dim node As GraphicsNode
    Set node = graphics.AddNode(1)
    node.Selectable = True
    node.DisplayName = "My Solid"

    Dim answer As VbMsgBoxResult
    answer = MsgBox("Yes=Node Selectable, No=All Selectable, Cancel=Every other face selectable", vbYesNoCancel + vbQuestion)

    Dim solidGraphics As SurfaceGraphics
    Set solidGraphics = node.AddSurfaceGraphics(body)
    ThisApplication.ActiveView.Update

    If answer = vbYes Then
        solidGraphics.ChildrenAreSelectable = False
    Else
        solidGraphics.ChildrenAreSelectable = True

        If answer = vbCancel Then
            Dim i As Integer
            For i = 1 To solidGraphics.DisplayedVertices.Count
                solidGraphics.DisplayedVertices.Item(i).Selectable = False
            Next

            For i = 1 To solidGraphics.DisplayedEdges.Count
                solidGraphics.DisplayedEdges.Item(i).Selectable = False
            Next

            For i = 1 To solidGraphics.DisplayedFaces.Count
                If i Mod 2 = 0 Then
                    solidGraphics.DisplayedFaces.Item(i).Selectable = False
                End If
            Next
        End If
    End If
End Sub
```
