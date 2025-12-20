# Edit thread features

## Description

The following example demonstrates how to edit an existing thread feature.

## Code Samples

* [VBA](#VBA)

You need to make sure that the ThreadInfo object that you create is appropriate (size, etc.) for the face that it will be applied for. A ThreadInfo object represents a row in the Thread.xls spreadsheet.

|  |
| --- |
| Copy Code |

```
Sub EditThread()
   Dim oDoc As PartDocument
   Set oDoc = ThisApplication.ActiveDocument

   Dim oDef As PartComponentDefinition
   Set oDef = oDoc.ComponentDefinition

   ' Create a new thread info object containing the thread data
   Dim oNewThreadInfo As StandardThreadInfo
   Set oNewThreadInfo = oDef.Features.ThreadFeatures.CreateStandardThreadInfo(False, True, "ISO Metric Profile", "M20x2.5", "6g")

   ' Get the first thread feature
   Dim oThread As ThreadFeature
   Set oThread = oDef.Features.ThreadFeatures.Item(1)

   ' Edit the thread feature
   oThread.ThreadInfo = oNewThreadInfo
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |