# Body Imprinting and matching the results

## Description

This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed.

## Code Samples

* [VBA](#VBA)

To use this sample you need to have a part with multiple bodies. Two of the bodies should be coincident and those two bodies can be selected when running the sample.

```
Public Sub SampleImprintMatching2()
    ' Get the active assembly document and its definition.
    Dim doc As PartDocument
    Set doc = ThisApplication.ActiveDocument
    Dim def As PartComponentDefinition
    Set def = doc.ComponentDefinition

    ' Have two parts selected in the assembly.
    Dim part1 As ComponentOccurrence
    Dim part2 As ComponentOccurrence
    Dim origBody1 As SurfaceBody
    Dim origBody2 As SurfaceBody
    Set origBody1 = ThisApplication.CommandManager.Pick(kPartBodyFilter, "Select body 1")
    Set origBody2 = ThisApplication.CommandManager.Pick(kPartBodyFilter, "Select body 2")

    ' Create alternate bodies.  Ideally this wouldn't be needed but this adds some special
    ' tags to the bodies that allow transient keys to continue to work after the ImprintBodies method is called.
    ' After this there is the original two bodies and the alternate version of each of the
    ' bodies.  The alternate may have more faces than the original, but the transient keys
    ' between the two should still match.
    Dim body1 As SurfaceBody
    Dim body2 As SurfaceBody
    Set body1 = origBody1.AlternateBody(Inventor.SurfaceGeometryFormEnum.SurfaceGeometryForm_NURBS)
    Set body2 = origBody2.AlternateBody(Inventor.SurfaceGeometryFormEnum.SurfaceGeometryForm_NURBS)

    ' Imprint the bodies.  After this call we now have three sets of bodies; the original, the alternate,
    ' and the imprinted bodies.  There should be additional faces in the imprinted bodies but the
    ' transient keys should still match for all three sets of bodies.
    Dim newBody1 As SurfaceBody
    Dim newBody2 As SurfaceBody
    Dim body1OverlapFaces As Faces
    Dim body2OverlapFaces As Faces
    Dim body1OverlapEdges As Edges
    Dim body2OverlapEdges As Edges
    Call ThisApplication.TransientBRep.ImprintBodies(body1, body2, True, newBody1, newBody2, body1OverlapFaces, body2OverlapFaces, body1OverlapEdges, body2OverlapEdges)

    ' The code below creates new non-parametric base features using the new imprinted bodies
    ' so that the results can be visualized.  The new bodies are created offset from the
    ' original so that they don't overlap and are more easily seen.
    '
    ' ** After this operation there will be four sets of bodies; the original, the alternate form,
    ' ** the imprinted bodies, and now the body created as a result of the feature creation.
    ' ** Because a new persisted body is created as part of the operation, new transient keys
    ' ** are assigned to the body, so the transient keys will no longer match this body.
    ' ** However, because they're essentially just copies of the imprinted bodies, the faces
    ' ** are in the same order in the two bodies so the indexes can be used to match between
    ' ** the two bodies.

    ' Define a matrix to use in transforming the bodies.
    Dim trans As Matrix
    Set trans = ThisApplication.TransientGeometry.CreateMatrix

    ' Move the first imprinted body over based on the range so it doesn't lie on the original.
    ' Moving the body is a modification of the existing body and leaves the transient keys as-is.
    ' However, it does change the face identities so comparing IUnknowns will no longer work.  Because
    ' of this I first save the indices of the overlapping faces while the faces are the same.
        Dim matchingIndexList1() As Integer
    Dim matchingIndexList2() As Integer
    ReDim matchingIndexList1(body1OverlapFaces.Count - 1)
    ReDim matchingIndexList2(body2OverlapFaces.Count - 1)
    Dim i As Integer
    For i = 1 To body1OverlapFaces.Count
        ' Find the indices of the overlapping face in the Faces collection.
        Dim j As Integer
        For j = 1 To newBody1.Faces.Count
            If body1OverlapFaces.Item(i) Is newBody1.Faces.Item(j) Then
                matchingIndexList1(i - 1) = j
                Exit For
            End If
        Next

        Dim body2Index As Integer
        For j = 1 To newBody2.Faces.Count
            If body2OverlapFaces.Item(i) Is newBody2.Faces.Item(j) Then
                matchingIndexList2(i - 1) = j
                Exit For
            End If
        Next
    Next

    ' Now do the transformation of the first body.
    trans.Cell(1, 4) = (body1.RangeBox.MaxPoint.X - body1.RangeBox.MinPoint.X) * 1.1
    Call ThisApplication.TransientBRep.Transform(newBody1, trans)

    ' Move the second imprinted body over based on the range so it doesn't lie on the original.
    trans.Cell(1, 4) = trans.Cell(1, 4) + (body1.RangeBox.MaxPoint.X - body1.RangeBox.MinPoint.X) * 1.1
    Call ThisApplication.TransientBRep.Transform(newBody2, trans)

    ' Create a new feature from the first imprinted body.
    Dim nonParaDef As NonParametricBaseFeatureDefinition
    Set nonParaDef = def.Features.NonParametricBaseFeatures.CreateDefinition
    Dim bodyColl As ObjectCollection
    Set bodyColl = ThisApplication.TransientObjects.CreateObjectCollection
    Call bodyColl.Add(newBody1)
    nonParaDef.BRepEntities = bodyColl
    nonParaDef.OutputType = kSolidOutputType
    Dim non1 As NonParametricBaseFeature
    Set non1 = def.Features.NonParametricBaseFeatures.AddByDefinition(nonParaDef)
    Dim resultBody1 As SurfaceBody
    Set resultBody1 = non1.SurfaceBodies.Item(1)

    ' Create a new feature from the second imprinted body.
    Set nonParaDef = def.Features.NonParametricBaseFeatures.CreateDefinition
    Set bodyColl = ThisApplication.TransientObjects.CreateObjectCollection
    Call bodyColl.Add(newBody2)
    nonParaDef.BRepEntities = bodyColl
    nonParaDef.OutputType = kSolidOutputType
    Dim non2 As NonParametricBaseFeature
    Set non2 = def.Features.NonParametricBaseFeatures.AddByDefinition(nonParaDef)
    Dim resultBody2 As SurfaceBody
    Set resultBody2 = non2.SurfaceBodies.Item(1)

    ' Fit the view to see the result.
    Dim cam As Camera
    Set cam = ThisApplication.ActiveView.Camera
    cam.Fit
    cam.Apply

    ' Create a highlight set used to see the matches.
    Dim hs As HighlightSet
    Set hs = doc.CreateHighlightSet

    ' Show the matches between the first imprint body and the original body.
    For i = 1 To newBody1.Faces.Count
        ' The face in the feature has a different transient key so get the
        ' face as the same index and assume it's the same.
        Dim newFace As Face
        Set newFace = resultBody1.Faces.Item(i)

        hs.AddItem newFace

        ' Get the corresponding face in the original body using the transient key from
        ' the imprinted face at the current index in the face collection.
        Dim otherFace As Face
        Set otherFace = origBody1.BindTransientKeyToObject(newBody1.Faces.Item(i).TransientKey)

        hs.AddItem otherFace

        MsgBox "Match"
        hs.Clear
    Next

    ' Show the matches between the second imprint body and the original body.
    For i = 1 To newBody2.Faces.Count
        ' The face in the feature has a different transient key so get the
        ' face as the same index and assume it's the same.
        Set newFace = resultBody2.Faces.Item(i)

        hs.AddItem newFace

        ' Get the corresponding face in the original body using the transient key from
        ' the imprinted face at the current index in the face collection.
        Set otherFace = origBody2.BindTransientKeyToObject(newBody2.Faces.Item(i).TransientKey)

        hs.AddItem otherFace

        MsgBox "Match"
        hs.Clear
    Next

    ' Highlight just the overlapping faces.
    ' The collection of overlapping faces returned by the ImprintBodies method correspond to
    ' the bodies returned by the ImprintBodies function.  This means the transient keys on the
    ' overlapping bodies will match all of the bodies except for the bodies created by the
    ' non-parametric base features.  The face index was save previously and will be used here.
    For i = 1 To body1OverlapFaces.Count
        Dim overlapFace1 As Face
        Dim overlapFace2 As Face
        Set overlapFace1 = resultBody1.Faces.Item(matchingIndexList1(i - 1))
        Set overlapFace2 = resultBody2.Faces.Item(matchingIndexList2(i - 1))

        hs.AddItem overlapFace1
        hs.AddItem overlapFace2

        MsgBox "Overlap Match"
        hs.Clear
    Next
End Sub
```
