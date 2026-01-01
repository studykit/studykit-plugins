# Inventor theme change sample

## Description

This sample demonstrates how to change the Inventor theme.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to change the Inventor theme.

```
Sub SwitchThemeSample()
    Dim oThemeManager As ThemeManager
    Set oThemeManager = ThisApplication.ThemeManager

    Dim oTheme As Theme, i As Long: i = 1
    Dim sNames As String, sName As String
    For Each oTheme In oThemeManager.Themes
        sNames = sNames & i & "): " & oTheme.Name & vbCrLf
        i = i + 1
    Next

    sName = InputBox("Which theme would you like to set: " & vbCrLf & vbCrLf & sNames, "Inventor")
    i = CInt(sName)

    If oThemeManager.Themes.Item(i).Name <> oThemeManager.ActiveTheme.Name Then
        oThemeManager.Themes.Item(i).Activate
    Else
        Call MsgBox("The selected theme is active, please select another theme.", vbOKOnly, "Inventor")
    End If

End Sub
```

This sample demonstrates how to change the Inventor theme.

```
Sub SwitchThemeSample()
    Dim oThemeManager As ThemeManager
    Set oThemeManager = ThisApplication.ThemeManager

    Dim oTheme As Theme, i As Long: i = 1
    Dim sNames As String, sName As String
    For Each oTheme In oThemeManager.Themes
        sNames = sNames & i & "): " & oTheme.Name & vbCrLf
        i = i + 1
    Next

    sName = InputBox("Which theme would you like to set: " & vbCrLf & vbCrLf & sNames, "Inventor")
    i = CInt(sName)

    If oThemeManager.Themes.Item(i).Name <> oThemeManager.ActiveTheme.Name Then
        oThemeManager.Themes.Item(i).Activate
    Else
        Call MsgBox("The selected theme is active, please select another theme.", vbOKOnly, "Inventor")
    End If

End Sub
```
