# DataIO

### Introduction to DataIO

Autodesk Inventor users can save their work or import from files in a variety of formats. For example, a part file can be saved as a SAT file, a STEP file, and so on. Autodesk Inventor can open files such as DWG, DXF, IGES, STEP, and so on. The type of format available is dependent on the context.

### The purpose of DataIO objects

To provide a similar level of functionality to the developer, many objects in the Autodesk Inventor API provide access to a DataIO object through a read-only DataIO property. The DataIO object provides methods to read from and write to files and data streams. In addition, the DataIO object provides methods to determine what formats and storage types are valid in that context. For example, a sketch can be saved as a DXF file, but cannot be imported from a bitmap.

The following is a list of Autodesk Inventor API objects that can return a DataIO object.

* AssemblyComponentDefinition* AttributeSet* AttributeSets* ComponentDefinition* DrawingSketch* DrawingView* PartComponentDefinition* PlanarSketch* PlanarSketchProxy* SectionDrawingView* Sheet* SheetMetalComponentDefinition* Sketch* SurfaceBody* SurfaceBodyProxy* WeldmentComponentDefinition* WeldsComponentDefinition

### Working with DataIO objects

As DataIO objects are available from such a variety of Autodesk Inventor API objects, so the context of the data to be read or written is variable. It is important to establish, in that context, whether data can be written or read, in what format, and whether to a file or data stream. Never just assume that a given format is valid.

The DataIO object supports two methods which determine available formats: *GetInputFormats* and *GetOutputFormats*. These methods each return a pair of arrays, identically dimensioned. The first array, Formats, contains the list of file formats in string form. For example, "XML" or "ACIS SAT." The second array contains *StorageTypeEnum* values. For example, *kFileStorage* indicates that storing as a file is supported.

Once the supported formats and storage types are known, the appropriate DataIO method can be used, with the format string passed to identify the required format. The output (write) methods are *WriteDataToFile* and *WriteDataToStream*. The input (read) methods are *ReadDataFromFile* and *ReadDataFromStream*. A file storage type is most typically used, but these methods also support streams. (For details on streams, see the Microsoft implementation of the IStream interface for structured storage).

### Example Format and StorageType arrays

The following tables depict DataIO object format and storage type array values that might be returned for a component definition in a part document. It shows Input (read) formats and Storage Types, returned by *GetInputFormats*.

|  |  |
| --- | --- |
| **Format Array** | **StorageType Array** |
| ACIS SAT | kFileStorage |
| ACIS SAB | kFileOrStreamStorage |

The following example shows output (write) Formats and Storage Types, returned by *GetOutputFormats*, for the same object.

|  |  |
| --- | --- |
| **Format Array** | **StorageType Array** |
| ACIS SAT | kFileStorage |
| ACIS SAB | kFileOrStreamStorage |
| ACIS SAT with TransientKeys | kFileStorage |
| ACIS SAB with TransientKeys | kFileOrStreamStorage |
| ACIS SAT with ProceduralToNURBS | kFileStorage |
| ACIS SAB with ProceduralToNURBS | kFileStorage |
| ACIS SAT with ProceduralToNURBS with TransientKeys | kFileStorage |
| ACIS SAB with ProceduralToNURBS with TransientKeys | kFileStorage |
| ACIS SAT with ProceduralToNURBS with TransientKeys DocUnits | kFileStorage |
| ACIS SAB with ProceduralToNURBS with TransientKeys DocUnits | kFileStorage |

These example arrays indicate that "ACIS SAT" is supported for read and write, but file storage only, while "ACIS SAB with TransientKeys" is supported for write-only, but with file or stream storage.

### How to use the API to determine available formats and storage types

This sample assumes an open part document containing a part, and looks at the supported DataIO formats for two objects: the *ComponentDefinition* and that object's *AttributeSets* object. A sequence of message boxes are posted containing the valid formats and storage types.

This code omits error checking for the sake of clarity and brevity. Always check that return values are of the expected type.

First, define a subroutine, and then obtain the active part document and its component definition object.

```vb
Sub query_dataIO()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument
    Dim oCompDef As ComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition
```

Declare the variables for the Format and StorageType arrays, and then get the DataIO object from the component definition.

```vb
Dim sFormats() As String
Dim sStorageTypes() As StorageTypeEnum
Dim oDataIO As DataIO
Set oDataIO = oCompDef.DataIO
```

Get the supported input (read) formats and display the results in a message box. However, first compose the message string - done by the ioPrint function, defined after this sub.

```vb
oDataIO.GetInputFormats sFormats, sStorageTypes
MsgBox ("CompDef Input: " & ioPrint(sFormats, sStorageTypes))
```

Get the supported output (write) formats and display the results in a message box, but first compose the message string - done by the ioPrint function, defined after this sub.

```vb
oDataIO.GetOutputFormats sFormats, sStorageTypes
MsgBox ("CompDef Output: " & ioPrint(sFormats, sStorageTypes))
End Sub
```

That completes the query\_dataIO subroutine. Now, define the ioPrint function. This is a utility function that takes the two arrays and pairs each format and storage type, returning a human-readable string. This function demonstrates that the format and storage type arrays always have identical dimensions. The *nth* item in the format array relates to the *nth* item in the storage type array.

```vb
Function ioPrint(sFormats As Variant, sStorageTypes As Variant) _
    As String
    Dim msgString As String
    Dim lindex As Long
    For lindex = 0 To UBound(sFormats)
        msgString = msgString & sFormats(lindex)
        Dim lType As StorageTypeEnum
        lType = sStorageTypes(lindex)
        Dim sType As String
        Select Case lType
        Case kFileOrStreamStorage
            msgString = msgString & "(File or Stream) "
        Case kFileStorage
            msgString = msgString & "(File) "
        Case kStorageStorage
            msgString = msgString & "(Storage) "
        Case kStreamStorage
            msgString = msgString & "(Stream) "
        Case kUnknownStorage
            msgString = msgString & "(Unknown) "
        End Select
    Next
    ioPrint = msgString
End Function
```

Running the query\_dataIO sub generates two message dialog boxes, containing something like the following examples.

CompDef Input: ACIS SAT (File) ACIS SAB (File or Stream)

CompDef Output: ACIS SAT (File) ACIS SAB (File or Stream)
ACIS SAT with TransientKeys (File) ACIS SAB with TransientKeys (File or Stream)

### Using the format and storage type information

This component definition supports writing to a SAT file. So it is valid to call *WriteDataToFile*, using the string "ACIS SAT" as the format, supplying a file name for storage, as in the following example.

```vb
oDataIO.WriteDataToFile "ACIS SAT", "c:\MyNewSATfile.SAT"
```

|  |
| --- |
| **Note:** Some supported file formats such as XML can have tags meaningful only in the given context, so it can be very helpful to use *WriteDataToFile* to produce a sample file to see that file's structure. |

In addition to using the DataIO object, files of many formats can be saved or opened through the *Open* or *SaveAs* methods of the *Document* object. The extension of the file name indicates to Autodesk Inventor which format is required.

### Summary

The Autodesk Inventor API supports reading and writing files in a variety of formats, depending on the context (object type). Many objects in the API provide access to a DataIO object. This object provides methods to determine what formats and storage types (file or stream) are valid in that context. The DataIO object supports methods to read and write to and from such valid formats.

### Also consider

Autodesk Inventor supports a type of Addin called a Translator Addin. This is much like a regular Addin, but is an Addin that reads and/or writes data in a specific, possibly proprietary, format. The Addin may do all the work or it may use an existing DataIO object. Such Addins are classed differently because they hook into Autodesk Inventor's File > Load and File > Save commands. For more information, refer to the TranslatorAddin object reference.