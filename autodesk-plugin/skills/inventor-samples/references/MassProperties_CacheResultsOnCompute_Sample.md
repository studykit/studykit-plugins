# Computing mass properties without dirtying document

## Description

This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences.

## Code Samples

* [VBA](#VBA)

To run the sample you must have a part document open that contains a solid.

|  |
| --- |
| Copy Code |

```
Public Sub GetPartMassPropsWithoutDirtying()
    ' Set a reference to the part document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Set a reference to the mass properties object.
    Dim oMassProps As MassProperties
    Set oMassProps = oPartDoc.ComponentDefinition.MassProperties

    'Check if mass property results are already available
    'at a high accuracy level or better. If so, simply
    'print out the results, else, set a flag to not cache
    'the results in the document.
    If oMassProps.AvailableAccuracy <> k_High And _
      oMassProps.AvailableAccuracy <> k_VeryHigh Then
      ' Set the accuracy to high.
      oMassProps.Accuracy = k_High

      'Set CacheResultsOnCompute property to False
      'so that results are not saved with the document
      'and hence the document is not 'dirtied'.
      oMassProps.CacheResultsOnCompute = False
    End If

    ' Display the mass properties of the part.
    Debug.Print "Area: " & oMassProps.Area

    Debug.Print "Center of Mass: " & _
    oMassProps.CenterOfMass.X & ", " & _
    oMassProps.CenterOfMass.Y & ", " & _
    oMassProps.CenterOfMass.Z

    Debug.Print "Mass: " & oMassProps.Mass
    Dim adPrincipalMoments(1 To 3) As Double
    Call oMassProps.PrincipalMomentsOfInertia(adPrincipalMoments(1), _
    adPrincipalMoments(2), _
    adPrincipalMoments(3))
    Debug.Print "Principal Moments of Inertia: " & _
    adPrincipalMoments(1) & ", " & _
    adPrincipalMoments(2) & ", " & _
    adPrincipalMoments(3)

    Dim adRadiusOfGyration(1 To 3) As Double
    Call oMassProps.RadiusOfGyration(adRadiusOfGyration(1), _
    adRadiusOfGyration(2), _
    adRadiusOfGyration(3))
    Debug.Print "Radius of Gyration: " & _
    adRadiusOfGyration(1) & ", " & _
    adRadiusOfGyration(2) & ", " & _
    adRadiusOfGyration(3)

    Debug.Print "Volume: " & oMassProps.Volume

    Dim Ixx As Double
    Dim Iyy As Double
    Dim Izz As Double
    Dim Ixy As Double
    Dim Iyz As Double
    Dim Ixz As Double
    Call oMassProps.XYZMomentsOfInertia(Ixx, Iyy, Izz, Ixy, Iyz, Ixz)
    Debug.Print "Moments: "
    Debug.Print " Ixx: " & Ixx
    Debug.Print " Iyy: " & Iyy
    Debug.Print " Izz: " & Izz
    Debug.Print " Ixy: " & Ixy
    Debug.Print " Iyz: " & Iyz
    Debug.Print " Ixz: " & Ixz
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |