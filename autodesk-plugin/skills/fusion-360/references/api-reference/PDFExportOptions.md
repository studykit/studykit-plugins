# PDFExportOptions Object

Derived from: [DrawingExportOptions](DrawingExportOptions.htm) Object

Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

Defines the inputs needed to export the drawing as PDF.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PDFExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filename](PDFExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. |
| [isValid](PDFExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PDFExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [openPDF](PDFExportOptions_openPDF.htm) | Specifies that the PDF file will be opened after export. |
| [sheetRange](PDFExportOptions_sheetRange.htm) | Defines the range of sheets to export. This can be a string like "1-3" or "1-2,5" where you can define a range of sheets and also specific sheets. Setting this property will automatically set the sheetsToExport setting to SelectedPDFSheets. |
| [sheetsToExport](PDFExportOptions_sheetsToExport.htm) | Defines which sheets to export. Defaults to AllPDFSheets which will create a single PDF file containing all sheets in the drawing.   the SelectedPDFSheets and CurrentPDFSheet options are dependent on the current selections in the user interface.   To set this to RangePDFSheets, use the sheetRange property to define the range of sheets to print. |
| [useLineWeights](PDFExportOptions_useLineWeights.htm) | Specifies if line weights should be used in the exported PDF file. |

## Accessed From

[DrawingExportManager.createPDFExportOptions](DrawingExportManager_createPDFExportOptions.htm)

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |