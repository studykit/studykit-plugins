# Mass Properties from Part

## Description

This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub GetPartMassProps()
    ' Set a reference to the part document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Set a reference to the mass properties object.
    Dim oMassProps As MassProperties
    Set oMassProps = oPartDoc.ComponentDefinition.MassProperties

    ' Set the accuracy to medium.
    oMassProps.Accuracy = k_Medium

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
    Debug.Print "   Ixx: " & Ixx
    Debug.Print "   Iyy: " & Iyy
    Debug.Print "   Izz: " & Izz
    Debug.Print "   Ixy: " & Ixy
    Debug.Print "   Iyz: " & Iyz
    Debug.Print "   Ixz: " & Ixz
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |