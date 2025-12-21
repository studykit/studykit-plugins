# Update iProperty values using Apprentice

## Description

Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist.

## Code Samples

* [VB.Net](#VB.Net)

Create a new VB.Net project and add a reference to the Inventor interop. Copy the code below into the project and call the function. For a Forms application you can call this when a button is clicked, or from a console application you can call it from the Main function. Please note that the sample works with Inventor version since Inventor 2022.2 or later versions which have the ApprenticeServerDocument.FilePropertySets, to work with Inventor 2022.1 or previous version you should change the ApprenticeServerDocument.FilePropertySets to ApprenticeServerDocument.PropertySets.

```
Public Sub ApprenticeUpdate()
    ' Declare a variable for Apprentice.
    Dim invApprentice As New Inventor.ApprenticeServerComponent

    ' Open a document using Apprentice.
    Dim invDoc As Inventor.ApprenticeServerDocument
    invDoc = invApprentice.Open("C:\Temp\Part1.ipt")

    ' Get the design tracking property set.
    Dim invDTProperties As Inventor.PropertySet
    invDTProperties = invDoc.FilePropertySets.Item("Design Tracking Properties")

    ' Edit the values of a couple of properties.
    invDTProperties.Item("Checked By").Value = "Bob"
    invDTProperties.Item("Date Checked").Value = Now

    ' Save the changes.
    invDoc.FilePropertySets.FlushToFile()

    ' Close the document and release all references.
    invDoc = Nothing
    invApprentice.Close()
    invApprentice = Nothing
End Sub
```
