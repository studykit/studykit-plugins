# Querying a sketch profile to get regions.

## Description

This sample demonstrates getting region properties from a sketch profile.

## Code Samples

* [VBA](#VBA)

To run the sample you must have a sketch active that contains some sketch entities.

```
Public Sub GetProfileRegionProperties()
    ' Set a reference to the active sketch.
    ' This assumes a 2D sketch is active.
    Dim oSketch As Sketch
    Set oSketch = ThisApplication.ActiveEditObject

    ' Create a default profile from the sketch.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Set a reference to the region properties object.
    Dim oRegionProps As RegionProperties
    Set oRegionProps = oProfile.RegionProperties

    ' Set the accuracy to medium.
    oRegionProps.Accuracy = kMedium

    ' Display the region properties of the profile.
    Debug.Print "Area: " & oRegionProps.Area

    Debug.Print "Perimeter: " & oRegionProps.Perimeter

    Debug.Print "Centroid: " & _
                    oRegionProps.Centroid.X & ", " & _
                    oRegionProps.Centroid.Y

    Dim adPrincipalMoments(1 To 3) As Double
    Call oRegionProps.PrincipalMomentsOfInertia(adPrincipalMoments(1), _
                                                    adPrincipalMoments(2), _
                                                    adPrincipalMoments(3))
    Debug.Print "Principal Moments of Inertia: " & _
                    adPrincipalMoments(1) & ", " & _
                    adPrincipalMoments(2)

    Dim adRadiusOfGyration(1 To 3) As Double
    Call oRegionProps.RadiusOfGyration(adRadiusOfGyration(1), _
                                            adRadiusOfGyration(2), _
                                            adRadiusOfGyration(3))
    Debug.Print "Radius of Gyration: " & _
                    adRadiusOfGyration(1) & ", " & _
                    adRadiusOfGyration(2)

    Dim Ixx As Double
    Dim Iyy As Double
    Dim Izz As Double
    Dim Ixy As Double
    Dim Iyz As Double
    Dim Ixz As Double
    Call oRegionProps.MomentsOfInertia(Ixx, Iyy, Izz, Ixy, Iyz, Ixz)
    Debug.Print "Moments: "
    Debug.Print " Ixx: " & Ixx
    Debug.Print " Iyy: " & Iyy
    Debug.Print " Ixy: " & Ixy

    Debug.Print "Rotation Angle from projected Sketch Origin to Principle Axes: " _
    & oRegionProps.RotationAngle

End Sub
```
