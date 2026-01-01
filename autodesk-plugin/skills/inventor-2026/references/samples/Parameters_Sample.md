# Model Parameters

## Description

This sample demonstrates the methods and properties supported by the Parameters object for model parameters.

## Code Samples

* [VBA](#VBA)

To run the sample you must have an part document open that contains at least one parameter, one of which is named d0.

```
Public Sub ModelParameters()
    ' Obtain the active document, this assumes
    ' that a part document is active in Inventor.
    Dim oPartDoc As Inventor.PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Obtain the Parameters collection
    Dim oParams As Parameters
    Set oParams = oPartDoc.ComponentDefinition.Parameters

    ' Iterate through the Parameters collection to obtain
    ' information about the Parameters
    Dim iNumParams As Long
    Debug.Print "ALL PARAMETERS"
    For iNumParams = 1 To oParams.Count
        'Display the Name
        Debug.Print " Name: " & oParams.Item(iNumParams).Name

        'Display the Parameter Type
        Select Case oParams.Item(iNumParams).Type
            Case kModelParameterObject
                Debug.Print "  Type: " & "Model Parameter"
            Case kTableParameterObject
                Debug.Print "  Type: " & "Table Parameter"
            Case kUserParameterObject
                Debug.Print "  Type: " & "User Parameter"
        End Select

        'Display the Value
        Debug.Print "  Value: " & oParams.Item(iNumParams).Value

        'Display the Health Status
        Select Case oParams.Item(iNumParams).HealthStatus
            Case kDeletedHealth
                Debug.Print "  Health Status: " & "Deleted"
            Case kDriverLostHealth
                Debug.Print "  Health Status: " & "Driver Lost"
            Case kInErrorHealth
                Debug.Print "  Health Status: " & "In Error"
            Case kOutOfDateHealth
                Debug.Print "  Health Status: " & "Out of Date"
            Case kUnknownHealth
                Debug.Print "  Health Status: " & "Unknown"
            Case kUpToDateHealth
                Debug.Print "  Health Status: " & "Up to Date"
        End Select
    Next iNumParams

    ' Obtain the Model Parameters collection
    Dim oModelParams As ModelParameters
    Set oModelParams = oParams.ModelParameters

    ' Iterate through the Model Parameters collection
    Dim iNumModelParams As Long
    Debug.Print "MODEL PARAMETER VALUES"
    For iNumModelParams = 1 To oModelParams.Count
        ' Display the Name
        Debug.Print " Name:" & oModelParams.Item(iNumModelParams).Name

        ' Display the Value
        Debug.Print "  Value: " & oModelParams.Item(iNumModelParams).Value

        ' Display the units
        Debug.Print "  Units: " & oModelParams.Item(iNumModelParams).Units

        ' Change the Model Parameter values
        oModelParams.Item(iNumModelParams).Value = oModelParams.Item(iNumModelParams).Value * 2
    Next iNumModelParams

    ' Accessing a particular parameter if you know its name, the user and reference parameters can also be accessed in a similar way
    oModelParams.Item("d0").Name = "NewParam"

    ' Change the value of the newly named parameter "param1"
    oModelParams.Item("NewParam").Value = 25

    ' Update the model.
    oPartDoc.Update
End Sub
```
