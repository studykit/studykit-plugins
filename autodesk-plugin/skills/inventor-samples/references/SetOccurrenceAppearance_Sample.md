# Set the appearance of an occurrence.

## Description

Sets the appearance of a selected occurrence in an assembly.

## Code Samples

* [VBA](#VBA)

```
Public Sub SetOccurrenceAppearance()
    Dim asmDoc As AssemblyDocument
    Set asmDoc = ThisApplication.ActiveDocument

    ' Get an appearance from the document.  To assign an appearance is must
    ' exist in the document.  This looks for a local appearance and if that
    ' fails it copies the appearance from a library to the document.
    Dim localAsset As Asset
    On Error Resume Next
    Set localAsset = asmDoc.Assets.Item("Bamboo")
    If Err Then
        On Error GoTo 0

        ' Failed to get the appearance in the document, so import it.

        ' Get an asset library by name.  Either the displayed name (which
        ' can changed based on the current language) or the internal name
        ' (which is always the same) can be used.
        Dim assetLib As AssetLibrary
        Set assetLib = ThisApplication.AssetLibraries.Item("Autodesk Appearance Library")
        'Set assetLib = ThisApplication.AssetLibraries.Item("314DE259-5443-4621-BFBD-1730C6CC9AE9")

        ' Get an asset in the library.  Again, either the displayed name or the internal
        ' name can be used.
        Dim libAsset As Asset
        Set libAsset = assetLib.AppearanceAssets.Item("Bamboo")
        'Set libAsset = assetLib.AppearanceAssets.Item("ACADGen-082")

        ' Copy the asset locally.
        Set localAsset = libAsset.CopyTo(asmDoc)
    End If
    On Error GoTo 0

    ' Have an occurrence selected.
    Dim occ As ComponentOccurrence
    Set occ = ThisApplication.CommandManager.Pick(kAssemblyOccurrenceFilter, "Select an occurrence.")

    ' Assign the asset to the occurrence.
    occ.appearance = localAsset
End Sub
```
