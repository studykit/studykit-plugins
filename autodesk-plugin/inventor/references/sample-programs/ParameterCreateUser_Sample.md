# Create user parameters

## Description

This sample demonstrates creating user parameters using an expression and a value. A part document must be open and it must not contain user parameters named "NewParam1" and "NewParam2".

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateParameters()
    ' Get the active document.  Assumes a part document is active.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Get the UserParameters collection
    Dim userParams As UserParameters
    Set userParams = partDoc.ComponentDefinition.Parameters.UserParameters

    ' Create a parameter using an expression.  The parameters unit is specified
    ' as millimeters, but the value of the parameter will be 3 inches because
    ' the unit is specified as part of the expression.
    Dim param As Parameter
    Set param = userParams.AddByExpression("NewParam1", "3 in", kMillimeterLengthUnits)

    ' Create a parameter using a value.  When setting by value, the value is always
    ' in database units.  In this case it is a length so it will always be in
    ' centimeters.  The units used for the parameter will be the current length units
    ' of the document because it's defined to use the default display length units.
    Set param = userParams.AddByValue("NewParam2", 3 * 2.54, kDefaultDisplayLengthUnits)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |