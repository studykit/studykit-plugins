# Show help sample with local help

## Description

The sample demonstrate how to set the help context/topic. Before running the sample you have to change the helpFile to specify it a correct Inventor API documentation path.

## Code Samples

* [VBA](#VBA)

The VBA sample demonstrate how to set the help context/topic to display help from a local chm file. Before running the sample you have to change the helpFile to specify it a with correct Inventor API documentation path.

```
Public Sub ShowHelpSampleWithLocalHelp()
    Dim helpFile As String
    helpFile = "C:\Users\Public\Documents\Autodesk\Inventor 20xx\Local Help\admapi_xx_0.chm"
    Call ThisApplication.HelpManager.DisplayHelpTopic(helpFile, "HTML\AliasFreeformFeature_ConsumeInputs.htm")
    Call ThisApplication.HelpManager.DisplayHelpContext(helpFile, 83886873)
End Sub
```
