# Write out all document appearances

## Description

This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance.

## Code Samples

* [VBA](#VBA)

```
Public Sub DumpDocumentAppearances()
    ' Check that a part or assembly document is active.
    If ThisApplication.ActiveDocumentType <> kAssemblyDocumentObject And ThisApplication.ActiveDocumentType <> kPartDocumentObject Then
        MsgBox "A part or assembly must be active."
        Exit Sub
    End If

    Dim doc As Document
    Set doc = ThisApplication.ActiveDocument

    ' Open a file to write the results.
    Open "C:\Temp\DocumentAppearanceDump.txt" For Output As #1

    Print #1, "Appearances in " & doc.FullFileName

    Dim appearance As Asset
    For Each appearance In doc.AppearanceAssets
        Print #1, "    Appearance"
        Print #1, "      DisplayName: " & appearance.DisplayName
        Print #1, "      HasTexture: " & appearance.HasTexture
        Print #1, "      IsReadOnly: " & appearance.IsReadOnly
        Print #1, "      Name: " & appearance.Name

        Dim value As AssetValue
        For Each value In appearance
            Call PrintAssetValue(value, 8)
        Next
    Next

    Close #1

    MsgBox "Finished writing output to ""C:\Temp\DocumentAppearanceDump.txt"""
End Sub

' Utility function that prints out information for the input asset value.
Private Sub PrintAssetValue(InValue As AssetValue, Indent As Integer)
    Dim indentChars As String
    indentChars = Space(Indent)

    Print #1, indentChars & "Value"
    Print #1, indentChars & "  DisplayName: " & InValue.DisplayName
    Print #1, indentChars & "  Name: " & InValue.Name
    Print #1, indentChars & "  IsReadOnly: " & InValue.IsReadOnly

    Select Case InValue.ValueType
        Case kAssetValueTextureType
            Print #1, indentChars & "  Type: Texture"

            Dim textureValue As TextureAssetValue
            Set textureValue = InValue

            Dim texture As AssetTexture
            Set texture = textureValue.value

            Select Case texture.TextureType
                Case kTextureTypeBitmap
                    Print #1, indentChars & "  TextureType: kTextureTypeBitmap"
                Case kTextureTypeChecker
                    Print #1, indentChars & "  TextureType: kTextureTypeChecker"
                Case kTextureTypeGradient
                    Print #1, indentChars & "  TextureType: kTextureTypeGradient"
                Case kTextureTypeMarble
                    Print #1, indentChars & "  TextureType: kTextureTypeMarble"
                Case kTextureTypeNoise
                    Print #1, indentChars & "  TextureType: kTextureTypeNoise"
                Case kTextureTypeSpeckle
                    Print #1, indentChars & "  TextureType: kTextureTypeSpeckle"
                Case kTextureTypeTile
                    Print #1, indentChars & "  TextureType: kTextureTypeTile"
                Case kTextureTypeUnknown
                    Print #1, indentChars & "  TextureType: kTextureTypeUnknown"
                Case kTextureTypeWave
                    Print #1, indentChars & "  TextureType: kTextureTypeWave"
                Case kTextureTypeWood
                    Print #1, indentChars & "  TextureType: kTextureTypeWood"
                Case Else
                    Print #1, indentChars & "  TextureType: Unexpected type returned"
            End Select

            Print #1, indentChars & "  Values"
            Dim textureSubValue As AssetValue
            For Each textureSubValue In texture
                Call PrintAssetValue(textureSubValue, Indent + 4)
            Next
        Case kAssetValueTypeBoolean
            Print #1, indentChars & "  Type: Boolean"

            Dim booleanValue As BooleanAssetValue
            Set booleanValue = InValue

            Print #1, indentChars & "    Value: " & booleanValue.value
        Case kAssetValueTypeChoice
            Print #1, indentChars & "  Type: Choice"

            Dim choiceValue As ChoiceAssetValue
            Set choiceValue = InValue

            Print #1, indentChars & "    Value: " & choiceValue.value

            Dim names() As String
            Dim choices() As String
            Call choiceValue.GetChoices(names, choices)
            Print #1, indentChars & "    Choices:"
            Dim i As Integer
            For i = 0 To UBound(names)
                Print #1, indentChars & "      " & names(i) & ", " & choices(i)
            Next
        Case kAssetValueTypeColor
            Print #1, indentChars & "  Type: Color"

            Dim colorValue As ColorAssetValue
            Set colorValue = InValue

            Print #1, indentChars & "  HasConnectedTexture: " & colorValue.HasConnectedTexture
            Print #1, indentChars & "  HasMultipleValues: " & colorValue.HasMultipleValues

            If Not colorValue.HasMultipleValues Then
                Print #1, indentChars & "  Color: " & ColorString(colorValue.value)
            Else
                Print #1, indentChars & "  Colors"

                Dim colors() As color
                colors = colorValue.Values

                For i = 0 To UBound(colors)
                    Print #1, indentChars & "    Color: " & ColorString(colors(i))
                Next
            End If
        Case kAssetValueTypeFilename
            Print #1, indentChars & "  Type: Filename"

            Dim filenameValue As FilenameAssetValue
            Set filenameValue = InValue

            Print #1, indentChars & "    Value: " & filenameValue.value
        Case kAssetValueTypeFloat
            Print #1, indentChars & "  Type: Float"

            Dim floatValue As FloatAssetValue
            Set floatValue = InValue

            Print #1, indentChars & "    Value: " & floatValue.value
        Case kAssetValueTypeInteger
            Print #1, indentChars & "  Type: Integer"

            Dim integerValue As IntegerAssetValue
            Set integerValue = InValue

            Print #1, indentChars & "    Value: " & integerValue.value
        Case kAssetValueTypeReference
            ' This value type is not currently used in any of the assets.
            Print #1, indentChars & "  Type: Reference"

            Dim refType As ReferenceAssetValue
            Set refType = InValue
        Case kAssetValueTypeString
            Print #1, indentChars & "  Type: String"

            Dim stringValue As StringAssetValue
            Set stringValue = InValue

            Print #1, indentChars & "    Value: """ & stringValue.value & """"
    End Select
End Sub

' Utility function that returns a string with the R,G,B,K values for an input Color object.
Private Function ColorString(InColor As color) As String
    ColorString = InColor.Red & "," & InColor.Green & "," & InColor.Blue & "," & InColor.Opacity
End Function
```
