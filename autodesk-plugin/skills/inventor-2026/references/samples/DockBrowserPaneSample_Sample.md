# Dock browser pane to a custom ViewFrame

## Description

This sample demonstrates how to dock the browser pane to a custom ViewFrame.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to dock the browser pane to a custom ViewFrame.

```
Sub DockBrowserPaneToCustomViewFrameSample()
    ' This sample demonstrates how to create a custom ViewFrame and dock the browser pane into it.

    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' This View of the new document is located in the default ViewFrame.
    Dim oView1 As View
    Set oView1 = oDoc.Views(1)

    Dim oViewTab1 As ViewTab
    Set oViewTab1 = oView1.ViewTab

    ' Create a new View for the same document.
    Dim oView2 As View
    Set oView2 = oDoc.Views.Add

    Dim oViewTab2 As ViewTab
    Set oViewTab2 = oView2.ViewTab

    ' Move the second View to generate a new custom ViewFrame, this will also activate the new ViewFrame.
    Dim oViewFrame1 As ViewFrame
    Set oViewFrame1 = oViewTab2.MoveToNewViewFrame(500, 600, 200, 100)

    Dim oBrowserPane As BrowserPane
    Set oBrowserPane = oDoc.BrowserPanes("PmDefault")

    oBrowserPane.SetDockingState kDockLeft, oViewFrame1

End Sub
```

This sample demonstrates how to dock the browser pane to a custom ViewFrame.

```
Sub DockBrowserPaneToCustomViewFrameSample()
    ' This sample demonstrates how to create a custom ViewFrame and dock the browser pane into it.

    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' This View of the new document is located in the default ViewFrame.
    Dim oView1 As View
    Set oView1 = oDoc.Views(1)

    Dim oViewTab1 As ViewTab
    Set oViewTab1 = oView1.ViewTab

    ' Create a new View for the same document.
    Dim oView2 As View
    Set oView2 = oDoc.Views.Add

    Dim oViewTab2 As ViewTab
    Set oViewTab2 = oView2.ViewTab

    ' Move the second View to generate a new custom ViewFrame, this will also activate the new ViewFrame.
    Dim oViewFrame1 As ViewFrame
    Set oViewFrame1 = oViewTab2.MoveToNewViewFrame(500, 600, 200, 100)

    Dim oBrowserPane As BrowserPane
    Set oBrowserPane = oDoc.BrowserPanes("PmDefault")

    oBrowserPane.SetDockingState kDockLeft, oViewFrame1

End Sub
```
