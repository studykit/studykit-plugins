# Move view tab between different view frames

## Description

This sample demonstrates how to move views using ViewTab between different view frames.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to move a View via its ViewTab to generate a new ViewFrame and move it to another ViewFrame.

```
Sub MoveViewTabSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oView1 As View
    Set oView1 = oDoc.Views(1)

    Dim oViewTab1 As ViewTab
    Set oViewTab1 = oView1.ViewTab

    Dim oView2 As View
    Set oView2 = oDoc.Views.Add

    Dim oViewTab2 As ViewTab
    Set oViewTab2 = oView2.ViewTab

    ' Move the second View to a new ViewFrame
    Dim oViewFrame As ViewFrame
    Set oViewFrame = oViewTab2.MoveToNewViewFrame(500, 600, 200, 100)

    Dim oDoc1 As PartDocument
    Set oDoc1 = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oView3 As View
    Set oView3 = oDoc1.Views(1)

    Dim oViewTab3 As ViewTab
    Set oViewTab3 = oView3.ViewTab

    ' Move the third View back to main frame.
    Call oViewTab3.MoveToGroup(True, oViewTab1, kDockBottom)
End Sub
```

This sample demonstrates how to move a View via its ViewTab to generate a new ViewFrame and move it to another ViewFrame.

```
Sub MoveViewTabSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oView1 As View
    Set oView1 = oDoc.Views(1)

    Dim oViewTab1 As ViewTab
    Set oViewTab1 = oView1.ViewTab

    Dim oView2 As View
    Set oView2 = oDoc.Views.Add

    Dim oViewTab2 As ViewTab
    Set oViewTab2 = oView2.ViewTab

    ' Move the second View to a new ViewFrame
    Dim oViewFrame As ViewFrame
    Set oViewFrame = oViewTab2.MoveToNewViewFrame(500, 600, 200, 100)

    Dim oDoc1 As PartDocument
    Set oDoc1 = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oView3 As View
    Set oView3 = oDoc1.Views(1)

    Dim oViewTab3 As ViewTab
    Set oViewTab3 = oView3.ViewTab

    ' Move the third View back to main frame.
    Call oViewTab3.MoveToGroup(True, oViewTab1, kDockBottom)
End Sub
```
