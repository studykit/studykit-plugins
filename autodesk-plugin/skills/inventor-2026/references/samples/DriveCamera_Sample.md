# Drive the camera

## Description

This sample will fly the camera around the model. To simplify the code, the target is hard coded at the origin and the up vector is the positive Z.

## Code Samples

* [VBA](#VBA)

```
Public Sub RotateCamera()
    ' Get the active camera.
    Dim cam As Camera
    Set cam = ThisApplication.ActiveView.Camera

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Define the number of steps in the animation.
    Dim steps As Integer
    steps = 360

    ' Define the distance between the eye and target.
    Dim eyeDistance As Double
    eyeDistance = 15

    ' Calculate pi.
    Dim pi As Double
    pi = Atn(1) * 4

    ' Iterate the specified number of steps.
    Dim i As Integer
    For i = 1 To steps
        ' Calculate the x and y coordinates of the eye.
        Dim x As Double
        Dim y As Double
        x = eyeDistance * Cos(i / steps * (2 * pi))
        y = eyeDistance * Sin(i / steps * (2 * pi))

        ' Set the eye with a hard coded z value.
        cam.Eye = tg.CreatePoint(x, y, 3)

        ' Define the up vector as positive z.
        cam.UpVector = tg.CreateUnitVector(0, 0, 1)

        ' Apply the current camera definition to the view.
        cam.ApplyWithoutTransition
    Next
End Sub
```
