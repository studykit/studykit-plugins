# Display information about parameter tolerances.

## Description

Dumps out information to the Immediate window about tolerance information associated with parameters. A part document must be active when this is run.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub DumpParamInfo()
    ' Get the active document assuming it is a part.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Get the component definition.  This owns the part specific info for the part.
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Get the parameters.  This collection contains all parameters, regardless
    ' of how they were created.
    Dim params As Parameters
    Set params = partDef.Parameters

    ' Get the model parameters.  This collection contains the parameters that were
    ' created as a by-product of creating something in Inventor that's driven
    ' by a parameter (dimension constraint, feature, work feature, etc.).
    Dim modelParams As ModelParameters
    Set modelParams = params.ModelParameters

    ' Iterate through the model parameters.
    Dim modelParam As ModelParameter
    For Each modelParam In modelParams
        Call DisplayToleranceInfo(modelParam)
    Next
End Sub

' Utility function used to display tolerance info for a parameter.
Private Sub DisplayToleranceInfo(Param As Parameter)
    ' Get the Tolerance object from the parameter.
    Dim tol As Tolerance
    Set tol = Param.Tolerance

    ' Display some info about the tolerance.
    Select Case tol.ToleranceType
        Case kDefaultTolerance
            Debug.Print "kDefaultTolerance"
        Case kBasicTolerance
            Debug.Print "kBasicTolerance"
        Case kDeviationTolerance
            Debug.Print "kDeviationTolerance"
        Case kLimitLinearTolerance
            Debug.Print "kLimitLinearTolerance"
        Case kLimitsFitsLinearTolerance
            Debug.Print "kLimitsFitsLinearTolerance"
        Case kLimitsFitsShowSizeTolerance
            Debug.Print "kLimitsFitsShowSizeTolerance"
        Case kLimitsFitsShowTolerance
            Debug.Print "kLimitsFitsShowTolerance"
        Case kLimitsFitsStackedTolerance
            Debug.Print "kLimitsFitsStackedTolerance"
        Case kLimitsStackedTolerance
            Debug.Print "kLimitsStackedTolerance"
        Case kMaxTolerance
            Debug.Print "kMaxTolerance"
        Case kMinTolerance
            Debug.Print "kMinTolerance"
        Case kOverrideTolerance
            Debug.Print "kOverrideTolerance"
        Case kReferenceTolerance
            Debug.Print "kReferenceTolerance"
        Case kSymmetricTolerance
            Debug.Print "kSymmetricTolerance"
    End Select

    Debug.Print "  Upper: " & tol.Upper
    Debug.Print "  Lower: " & tol.Lower
    Debug.Print "  Hole: " & tol.HoleTolerance
    Debug.Print "  Shaft: " & tol.ShaftTolerance
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |