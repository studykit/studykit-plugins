# Apprentice Server

## Using Apprentice Server

The simple way to think of Apprentice is that it's a smaller version
of Autodesk Inventor that does not have a user interface. Without a
user interface the only way to access its functionality is by using its
API. Apprentice is actually an ActiveX component. It runs within the
process space of the client that's using it. For example, if you write
a Visual Basic program that displays information about the contents of
an assembly, Apprentice will be running within your VB program's
process space. Apprentice can be very efficient for certain
applications because it's smaller than the complete Autodesk Inventor
application and because it runs in the same process as your application.

**Note: Apprentice is not supported within Inventor itself. Do not run it in an Inventor addin nor in a VBA macro.**

The API exposed by Apprentice is a subset of the complete Autodesk
Inventor API. Apprentice provides access to file references, assembly
structure, B-Rep, geometry, render styles, and document
properties. Access to the assembly structure, B-Rep, geometry and render
styles is read-only. Access to file references and
document properties is read and write. In past releases of the product,
a type library specifically for Apprentice was delivered with both
Autodesk Inventor and Apprentice. This type library contained the
limited set of objects supported only by Apprentice. Now, however,
since the Autodesk Inventor type library contains all of the Apprentice
functionality, this should be used in an Apprentice context. A version
of the old Apprentice type library is still supplied for legacy
reasons, but this will likely be discontinued in future releases.

Some common types of applications that will make use of Apprentice
are larger standalone applications that want to be able to use Autodesk
Inventor files. For example, an existing NC application could use
Apprentice to directly read in an Autodesk Inventor part or assembly.
If it were to use Autodesk Inventor for this it would need to start
Autodesk Inventor first, use Autodesk Inventor's API to open the
desired document, and then use Autodesk Inventor's API to query for
necessary information. There's a lot of unnecessary overhead in having
to start Autodesk Inventor and a significant performance penalty caused
by all of the API calls going between two processes. These problems are
solved with Apprentice since it is very lightweight and runs in the
process space of the application.

Another feature of Apprentice is the cost. Apprentice is freely
available and is distributed as part of Design Tracking, which is
available for download from the Autodesk website. Much of Design
Tracking actually uses Apprentice.

A simpler example of the use of Apprentice is a small application
that updates the cost property of an Autodesk Inventor part document
based on the current cost that is stored in a business database. In
this case Apprentice is being used to write the document properties of
a part. The utility can quickly go through a set of Autodesk Inventor
part documents and set the cost property with a value it obtained from
a database.

Most of the features that Apprentice supports are identical to those
in Autodesk Inventor. For example, to traverse an assembly you would
perform the traversal the same way in Apprentice as you would in
Autodesk Inventor. The basic traversal function can be written to be
used for both cases. Because most of the API supported by Apprentice is
the same as Autodesk Inventor's, this section on Apprentice will focus
on the differences between the two.

The primary differences between Autodesk Inventor and Apprentice are
in the Application and Document objects. The objects that represent the
Application and Document are completely different in Autodesk Inventor
and Apprentice. The Apprentice Application object is called
ApprenticeServerComponent. It supports a much more limited API than the
Inventor Application object. In Apprentice there isn't a Documents
collection.

When ApprenticeServer.Open opens a document, a reference to that
document is held by the ApprenticeServer component in order to be
returned from the ApprenticeServer.Document. This ‘active top/last
opened’ document is also considered the document used as the root of
the save for the FileSaveAs object. A document is closed when either
ApprenticeServerDocument.Close is called, or the document’s reference
count fully drops to zero. Keep in mind that the reference held by the
ApprenticeServer (if it was the last document to be opened) also counts
as a reference. This ApprenticeServer reference will be released either
when a different document is opened, or ApprenticeServer.Close is
called, or when the ApprenticeServer’s reference count fully drops to
zero and it is destroyed.

The ApprenticeServerComponent supports a few methods and properties
that are unique to Apprentice. These are the Open and Close methods,
which are used to open and close documents within Apprentice;
DisplayAffinity, which is used to optimize the behavior of Apprentice
for viewer applications; MinimizeFileSize, which compresses files by
removing versions, and FileSaveAs, which we'll discuss in more detail
later in this section.

The document objects used within Apprentice are different from the
document objects used in Autodesk Inventor. In Inventor there are the
PartDocument, AssemblyDocument, DrawingDocument, and
PresentationDocument objects. In Apprentice, the
ApprenticeServerDocument object represents the part, assembly, and
presentation documents and the ApprenticeServerDrawingDocument
represents the drawing document. The code below illustrates using
Apprentice to open a document.

```vb
Private Sub TestApprentice()
    ' Create a new instance of Apprentice.
    Dim oApprentice As New ApprenticeServerComponent
    ' Open a document.
    Dim oDoc As ApprenticeServerDocument
    Set oDoc = oApprentice.Open("C:\Temp\Assembly1.iam")
End Sub
```

The "New" keyword is used in the declaration of the variable for the
ApprenticeServerComponent. This creates a new instance of an object of
ApprenticeServerComponent type. Apprentice isn't actually loaded at
this point, but is loaded the first time the variable is used--in this
case, when the Open method of Apprentice is called.

Even though there are differences between the application and
document objects of Autodesk Inventor and Apprentice, once you get past
these top-level objects, the objects below them in the hierarchy are
the same. For example, a function that extracts information from the
B-Rep or from an assembly can be used with Autodesk Inventor or
Apprentice without any changes. The function below will display an
assembly tree given a ComponentOccurrences object regardless of whether
it is used in Apprentice or Autodesk Inventor.

```vb
Private Sub GetComponents(InCollection As ComponentOccurrences, _ Level As Long)
    ' Iterate through the components in the current collection.
    Dim oCompOccurrence As ComponentOccurrence
    For Each oCompOccurrence In InCollection
        ' Display information about the current component.
        Debug.Print Space(Level * 3) & oCompOccurrence.Name
        ' Recursively call this function for the suboccurrences
        ' of the current component.
        Call GetComponents(oCompOccurrence.SubOccurrences, Level + 1)
    Next
End Sub
```

Here's a modified version of the earlier sample that connects to
Apprentice and opens a document. It's been updated to check for the
document type and then call the GetComponents function above.

```vb
Private Sub TestApprentice()
    ' Create a new instance of Apprentice.
    Dim oApprentice As New ApprenticeServerComponent
    ' Open a document.
    Dim oDoc As ApprenticeServerDocument
    Set oDoc = oApprentice.Open("C:\Temp\Assembly1.iam")
    ' Display this document's name.
    Debug.Print oDoc.DisplayName
    ' Check to make sure the document is an assembly.
    If oDoc.DocumentType = kAssemblyDocument Then
        ' Show the occurrence tree.
        Call GetComponents(oDoc.ComponentDefinition.Occurrences, 1)
    End If
End Sub
```

Because Apprentice provides read-only access to some of the
information in an Autodesk Inventor document, some of the properties on
objects may fail when you attempt to set them. For example, the Name
property of the ComponentOccurrence object behaves as read-only in
Apprentice, whereas in Autodesk Inventor it is read-write. The B-Rep
portion of the API behaves identically in Autodesk Inventor and
Apprentice since it provides query-only access in both cases.

There are a few things that can only be done using Apprentice. These
are all things that cause problems when the file is open in Inventor
but can be easily accomplished when accessed through Apprentice. One of
the most important of these is the ability to change file references.
This is a critical part of Apprentice that Design Assistant uses. For
example, let's say you have an assembly that contains Part1 and Part2.
Part1 needs to be revised so you make a copy of the file, give it a new
name, make the changes to the part, and save it. When you open the
assembly it's still referencing the old file. The file reference
portion of the API allows you to change the reference within the
assembly so that it's pointing to the file that represents the revised
version of Part1.

The FileSaveAs object, which is only available in Apprentice,
provides functionality that lets you save components of an assembly to
different filenames and update the assembly's references to point to
the new files.

Using the FileSaveAs object you can save the document you currently
have open. If you make any changes to the document you must use the
FileSaveAs object to save those changes, otherwise it's equivalent to
exiting the file without saving. The sample below opens an assembly,
looks for a reference to a specific file, changes the reference to
point to another file, and then saves the change.

```vb
Private Sub ChangeReferenceSample()
    Dim oApprentice As New ApprenticeServerComponent
    ' Open a document.
    Dim oDoc As ApprenticeServerDocument
    Set oDoc = oApprentice.Open("C:\Temp\Assembly1.iam")
    ' Iterate through the references looking for a
    ' reference to a specific file.
    Dim oRefFileDesc As ReferencedFileDescriptor
    For Each oRefFileDesc In oDoc.ReferencedFileDescriptors
        If oRefFileDesc.FullFileName = "C:\Temp\OldPart.ipt" Then
            ' Replace the reference.
            Call oRefFileDesc.PutLogicalFileNameUsingFull( _                                              "C:\Temp\NewPart.ipt")
            Exit For
        End If
    Next
    '
    Set a reference to the FileSaveAs object.
    Dim oFileSaveAs As FileSaveAs
    Set oFileSaveAs = oApprentice.FileSaveAs
    ' Save the assembly.
    Call oFileSaveAs.AddFileToSave(oDoc, oDoc.FullFileName)
    Call oFileSaveAs.ExecuteSave
End Sub
```

If you're using Apprentice to access the document properties, and
that's the only edit you've made to the document, you don't need to use
the FileSaveAs object to save the file, but can use the FlushToFile
method of the PropertySets object to save the property changes. This is
much more efficient because it only writes the properties to the
document and doesn't write the entire document.

Please note: Saving of files in Apprentice
is not allowed on files that require migration (any file that has not
already been migrated to the same version of the Apprentice server).
The current document's NeedsMigrating property must return False before
the FileSaveAs object can successfully be returned.

### How to get Apprentice Server installed on machine?

To access Apprentice API you should have Apprentice Server installed on your machine, there are three ways to have Apprentice Server installed on your machine:

1. Install Inventor. When you have Inventor installed, you have Apprentice Server installed along with it.
2. Install Apprentice Server standlone installer(Since Inventor Apprentice Server 2022). The [Autodesk website](https://knowledge.autodesk.com/support/inventor/downloads) can be used to search download link for Inventor Apprentice Server standlone installer since [Inventor Apprentice Server 2022](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/1mEGM3fEESw2c0dNlXzkAU.html).